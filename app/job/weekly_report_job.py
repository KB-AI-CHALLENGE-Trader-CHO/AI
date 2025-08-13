import logging
from datetime import date

from fastapi import FastAPI
from langsmith import traceable
from sqlalchemy import func

from app.ai.chain import weekly_report_chain
from app.database import SessionLocal
from app.models import WeeklyAnalysis, WeeklyReport

logger = logging.getLogger(__name__)


# 매주 일요일 00시 00분 진행
@traceable(name="주간 매매 종합 분석 cron job")
async def weekly_report_job(app: FastAPI) -> None:
    db = SessionLocal()
    weekly_analyses = (db.query(WeeklyAnalysis)
                       .filter(func.yearweek(WeeklyAnalysis.date_time) == func.yearweek(func.curdate()))
                       .all())

    weekly_report = await weekly_report_chain.ainvoke(
        prompt_parameter={"suggestions": [weekly_analysis.suggestion for weekly_analysis in weekly_analyses]}
    )

    weekly_report_tuple = WeeklyReport(period=date.today(), summary=weekly_report.summary)
    db.add(weekly_report_tuple)
    db.flush()
    for i in range(len(weekly_analyses)):
        weekly_analyses[i].weekly_report_id = weekly_report_tuple.id

    logging.info(f"주간 분석 cron job 실행 완료: {date.today()}")
    db.commit()
