from contextlib import asynccontextmanager

from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from app.ai.chain import test_chain
from app.config import settings
from app.job.job_manager import JobManager, test_job

logging.basicConfig(level=logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
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
job_manager.register_jobs(test_job, IntervalTrigger(seconds=5), "test_job")

@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/health")
async def health_check():
    return {"code": 200, "status": "healthy"}


@app.get("/test")
async def run_test_chain():
    return await test_chain.ainvoke()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )
