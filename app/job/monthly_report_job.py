import logging
from collections import defaultdict
from datetime import date, datetime
from itertools import islice

from fastapi import FastAPI
from langsmith import traceable
from sqlalchemy import func, text

from app.ai.chain import monthly_stock_report_chain, monthly_report_chain
from app.database import SessionLocal
from app.models import WeeklyAnalysis, TradeHistory, MonthlyAnalysis, MonthlyReport

logger = logging.getLogger(__name__)

MONTHLY_STOCK_REPORT_BATCH_JOB_SIZE = 5
MONTHLY_REPORT_BATCH_JOB_SIZE = 5


# 매달 첫날 00시 00분 실행(이전달 평가)
@traceable(name="월간 매매 종합 분석 cron job")
async def monthly_report_job(app: FastAPI) -> None:
    db = SessionLocal()
    trade_reports = (db.query(WeeklyAnalysis.suggestion)
                     .filter(func.date_format(WeeklyAnalysis.date_time, "%Y%m") == func.date_format(func.date_sub(func.curdate(), text("INTERVAL 1 MONTH")), "%Y%m"))
                     .all())
    monthly_report = await monthly_report_chain.ainvoke(prompt_parameter={"trade_reports": trade_reports})

    db.add(MonthlyReport(
        period=date.today(),
        summary=monthly_report.summary
    ))
    logging.info(f"월간 종합 분석 cron job 실행 완료: {date.today()}")
    db.commit()



# 매달 첫날 00시 05분 실행(이전달 평가)
@traceable(name="월간 단일 종목 매매 종합 분석 cron job")
async def monthly_stock_report_job(app: FastAPI) -> None:
    db = SessionLocal()
    stock_suggestions = (db.query(TradeHistory.stock_item_id, WeeklyAnalysis.suggestion)
                         .join(TradeHistory, WeeklyAnalysis.history_id == TradeHistory.id)
                         .filter(func.date_format(WeeklyAnalysis.date_time, "%Y%m") == func.date_format(func.date_sub(func.curdate(), text("INTERVAL 1 MONTH")), "%Y%m"))
                         .all())
    monthly_report_id = (db.query(MonthlyReport.id)
                         .filter(func.date_format(WeeklyAnalysis.date_time, "%Y%m") == func.date_format(func.date_sub(func.curdate(), text("INTERVAL 1 MONTH")), "%Y%m"))
                         .first()[0])

    stock_dict = defaultdict(list)
    for stock_item_id, suggestion in stock_suggestions:
        stock_dict[stock_item_id].append(suggestion)
    stock_item_ids, stock_item_suggestions = zip(*stock_dict.items())
    stock_item_suggestions = [{"stock_suggestions": stock_item_suggestion} for stock_item_suggestion in stock_item_suggestions]

    monthly_stock_reports, stock_item_len = [], len(stock_item_ids)
    stock_item_suggestions_iter = iter(stock_item_suggestions)
    while chunk := list(islice(stock_item_suggestions_iter, MONTHLY_STOCK_REPORT_BATCH_JOB_SIZE)):
        monthly_stock_reports.extend(await monthly_stock_report_chain.abatch(prompt_parameter=chunk, batch_size=MONTHLY_STOCK_REPORT_BATCH_JOB_SIZE))

    for i in range(stock_item_len):
        db.add(MonthlyAnalysis(
            stock_item_id=stock_item_ids[i],
            monthly_report_id=monthly_report_id,
            date_time=datetime.now(),
            analysis_details=monthly_stock_reports[i].analysis_details,
            suggestion=monthly_stock_reports[i].suggestion))
    logging.info(f"월간 종목 분석 cron job 실행 완료: {date.today()}")
    db.commit()
