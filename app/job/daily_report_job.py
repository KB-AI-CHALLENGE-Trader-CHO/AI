import logging
from datetime import date, timedelta
from itertools import islice

from fastapi import FastAPI
from langsmith import traceable
from sqlalchemy import func
from sqlalchemy.orm import selectinload

from app.ai.chain import trade_report_chain
from app.database import SessionLocal
from app.models import TradeHistory
from app.models.trade_evaluation import TradeEvaluation

logger = logging.getLogger(__name__)

TRADE_REPORT_BATCH_JOB_SIZE = 5


# 매일 매일 진행
@traceable(name="매매별 분석 cron job")
async def trade_report_job(app: FastAPI) -> None:
    db = SessionLocal()
    trade_evaluations = (db.query(TradeEvaluation)
                         .options(selectinload(TradeEvaluation.trade_history).selectinload(TradeHistory.weekly_analysis))
                         .filter(func.date(TradeEvaluation.evaluated_at) == date.today() - timedelta(days=1))
                         .all())
    trade_evaluation_dicts = [{"trade_evaluation": trade_evaluation.to_dict(),
                               "trade_history": trade_evaluation.trade_history.to_dict()}
                              for trade_evaluation in trade_evaluations]

    trade_reports, trade_evaluations_len = [], len(trade_evaluations)
    trade_evaluation_dicts_iter = iter(trade_evaluation_dicts)
    while chunk := list(islice(trade_evaluation_dicts_iter, TRADE_REPORT_BATCH_JOB_SIZE)):
        trade_reports.extend(await trade_report_chain.abatch(prompt_parameter=chunk, batch_size=TRADE_REPORT_BATCH_JOB_SIZE))

    for i in range(trade_evaluations_len):
        trade_evaluations[i].trade_history.weekly_analysis.suggestion = trade_reports[i].get_suggestions_string()
    logging.info(f"매매별 분석 cron job 실행 완료: {date.today()}")
    db.commit()
