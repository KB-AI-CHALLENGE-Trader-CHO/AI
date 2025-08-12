import logging
from datetime import date

from fastapi import FastAPI
from langsmith import traceable
from sqlalchemy import func

from app.ai.chain import trade_report_chain
from app.database import SessionLocal
from app.models.trade_evaluation import TradeEvaluation

logger = logging.getLogger(__name__)

TRADE_REPORT_BATCH_JOB_SIZE = 5


# 매일 매일 진행
@traceable(name="매매별 분석 cron job")
async def trade_report_job(app: FastAPI, trade_reports=None) -> None:
    db = SessionLocal()
    evaluated_trades = db.query(TradeEvaluation).filter(func.date(TradeEvaluation.evaluated_at) == date.today()).all()
    trade_evaluations = [
        {"trade_evaluation": evaluated_trade.to_dict(),
         "trade_info": evaluated_trade.trade_history.to_dict()} for evaluated_trade in evaluated_trades
    ]

    trade_evaluations_len = len(trade_evaluations)
    for i in range(0, len(trade_evaluations), TRADE_REPORT_BATCH_JOB_SIZE):
        trade_reports.extend(await trade_report_chain.abatch(
            prompt_parameter=trade_evaluations[
                             i:i + TRADE_REPORT_BATCH_JOB_SIZE if trade_evaluations_len > i + TRADE_REPORT_BATCH_JOB_SIZE
                             else trade_evaluations_len],
            batch_size=TRADE_REPORT_BATCH_JOB_SIZE))

    for i in range(5):
        if evaluated_trades[i].trade_history.weekly_analyses is None:
            logging.info(f"매매 분석 데이터 미존재")
            raise Exception()
        evaluated_trades[i].trade_history.weekly_analyses.suggestion = trade_reports[i].get_suggestions_string()
    logging.info(f"매매별 분석 cron job 실행 완료: {date.today()}")
    db.commit()
