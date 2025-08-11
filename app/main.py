from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from app.ai.chain import test_chain, trade_report_chain
from app.config import settings
from app.job.job_manager import JobManager
from app.schemas.daily_context import test_daily_context
from app.schemas.intraday_timing import test_intraday_timing
from app.schemas.trade_info import test_trade_info

logging.basicConfig(level=logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # job_manager.register_jobs(test_job, IntervalTrigger(seconds=5), "test_job")
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


@app.get("/trade-report")
async def trade_report():
    return await trade_report_chain.ainvoke({
        "trade_info": test_trade_info,
        "daily_context": test_daily_context,
        "intraday_timing": test_intraday_timing
    })
