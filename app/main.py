from contextlib import asynccontextmanager

from apscheduler.triggers.cron import CronTrigger
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.ai.chain import test_chain
from app.config import settings
from app.job import trade_report_job, weekly_report_job, monthly_stock_report_job, monthly_report_job
from app.job.job_manager import JobManager


@asynccontextmanager
async def lifespan(app: FastAPI):
    job_manager.register_jobs(trade_report_job, CronTrigger(hour=0, minute=0), "trade_report_job")
    job_manager.register_jobs(weekly_report_job, CronTrigger(day_of_week="sun", hour=0, minute=0), "weekly_report_job")
    job_manager.register_jobs(monthly_report_job, CronTrigger(day="1", hour=0, minute=0), "monthly_report_job")
    job_manager.register_jobs(monthly_stock_report_job, CronTrigger(day="1", hour=0, minute=5),
                              "monthly_stock_report_job")
    job_manager.start_scheduler()
    yield
    job_manager.shutdown_scheduler()


app = FastAPI(
    title="AI Backend",
    description="AI Backend Server",
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

job_manager = JobManager(app)


@app.get("/health")
async def health_check():
    return {"code": 200, "status": "healthy"}


@app.get("/test")
async def run_test_chain():
    return await test_chain.ainvoke({})
