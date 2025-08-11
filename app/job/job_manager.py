from apscheduler.schedulers.asyncio import AsyncIOScheduler
import pytz
import logging
from typing import Callable, Any

from fastapi import FastAPI

logger = logging.getLogger(__name__)


class JobManager:

    def __init__(self, app: FastAPI):
        self.app = app
        self.scheduler = AsyncIOScheduler(timezone=pytz.timezone("Asia/Seoul"))

    def register_jobs(self, job: Callable[..., Any], trigger, id: str) -> None:
        job_defaults = {
            "coalesce": True,  # 지연되면 여러 번 대신 한 번만 실행
            "misfire_grace_time": 60 * 30,  # 최대 30분까지 지연 허용
            "max_instances": 1,  # 중복 실행 방지
        }
        self.scheduler.configure(job_defaults=job_defaults)

        self.scheduler.add_job(
            job,
            trigger=trigger,
            id=id,
            replace_existing=True,
            kwargs={"app": self.app}
        )
        logger.info(f"Job '{id}' registered with trigger: {trigger}")

    def start_scheduler(self) -> None:
        if not self.scheduler.running:
            self.scheduler.start()
            logger.info("Scheduler started")

    def shutdown_scheduler(self) -> None:
        if self.scheduler.running:
            self.scheduler.shutdown(wait=False)
            logger.info("Scheduler stopped")


async def test_job(app: FastAPI) -> None:
    logger.info("test job started")
    print("시작된")
