from sqlalchemy import BigInteger, Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import DATE

from .base import Base


class WeeklyReport(Base):
    __tablename__ = "weekly_report"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    period = Column(DATE, nullable=False)
    summary = Column(String(500), nullable=True)

    # 관계 설정
    weekly_analyses = relationship("WeeklyAnalysis", back_populates="weekly_report")
