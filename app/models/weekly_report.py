from sqlalchemy import Column
from sqlalchemy.dialects.mysql import DATE, BIGINT, VARCHAR
from sqlalchemy.orm import relationship

from .base import Base


class WeeklyReport(Base):
    __tablename__ = "weekly_report"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    period = Column(DATE, nullable=False)
    summary = Column(VARCHAR(500), nullable=True)

    # 관계 설정
    weekly_analyses = relationship("WeeklyAnalysis", back_populates="weekly_report")
