import logging
from datetime import date, datetime

from fastapi import FastAPI
from langsmith import traceable
from sqlalchemy import func

from app.ai.chain import monthly_stock_report_chain, monthly_report_chain
from app.database import SessionLocal
from app.models import WeeklyAnalysis, TradeHistory, MonthlyAnalysis, MonthlyReport

logger = logging.getLogger(__name__)

MONTHLY_STOCK_REPORT_BATCH_JOB_SIZE = 5


# 매달 첫날 00시 00분 실행(이전달 평가)
@traceable(name="월간 종목 분석 cron job")
async def monthly_stock_report_job(app: FastAPI) -> None:
    db = SessionLocal()
    rows = (
        db.query(TradeHistory.stock_item_id, WeeklyAnalysis.suggestion)
        .join(TradeHistory, WeeklyAnalysis.history_id == TradeHistory.id)
        .filter(func.date_format(WeeklyAnalysis.date_time, "%Y-%m") == func.date_format(
            func.date_sub(func.curdate(), func.interval(1, "month")), "%Y-%m"))
        .all()
    )
    stock_dict = dict()
    for stock_item_id, suggestion in rows:
        if stock_item_id not in stock_dict:
            stock_dict[stock_item_id] = [suggestion]
        else:
            stock_dict[stock_item_id].append(suggestion)

    stock_item_ids, stock_item_reports = zip(*stock_dict.items())
    stock_item_len = len(stock_item_ids)
    stock_item_reports = [{"stock_reports": stock_item_report} for stock_item_report in stock_item_reports]

    monthly_stock_reports = []
    for i in range(0, stock_item_len, MONTHLY_STOCK_REPORT_BATCH_JOB_SIZE):
        monthly_stock_reports.extend(await monthly_stock_report_chain.abatch(
            prompt_parameter=stock_item_reports[i:i + MONTHLY_STOCK_REPORT_BATCH_JOB_SIZE
            if stock_item_len >= i + MONTHLY_STOCK_REPORT_BATCH_JOB_SIZE else stock_item_len],
            batch_size=MONTHLY_STOCK_REPORT_BATCH_JOB_SIZE))

    for i in range(stock_item_len):
        db.add(MonthlyAnalysis(
            stock_item_id=stock_item_ids[i],
            date_time=datetime.now(),
            analysis_details="무슨 값을 넣어야 하나",
            suggestion=stock_item_reports[i].analysis_detail
        ))
    logging.info(f"월간 종목 분석 cron job 실행 완료: {date.today()}")
    db.commit()


# 매달 첫날 00시 00분 실행
@traceable(name="월간 종합 분석 cron job")
async def monthly_report_job(app: FastAPI) -> None:
    db = SessionLocal()
    rows = (
        db.query(WeeklyAnalysis).filter(func.date_format(WeeklyAnalysis.date_time, "%Y-%m") == func.date_format(
            func.date_sub(func.curdate(), func.interval(1, "month")), "%Y-%m"))
        .all()
    )
    monthly_report = await monthly_report_chain.ainvoke(prompt_parameter={"trade_reports": rows})

    db.add(MonthlyReport(
        period=date.today(),
        summary=monthly_report.summary
    ))
    logging.info(f"월간 종합 분석 cron job 실행 완료: {date.today()}")
    db.commit()
