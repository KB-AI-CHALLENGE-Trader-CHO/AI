from sqlalchemy import BigInteger, Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import DATE
from .base import Base


class MonthlyReport(Base):
    __tablename__ = "monthly_report"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    period = Column(DATE, nullable=False)
    summary = Column(String(500), nullable=True)

    # 의존 관계 설정
    monthly_analyses = relationship("MonthlyAnalysis", back_populates="monthly_report")
    weekly_analyses = relationship("WeeklyAnalysis", back_populates="monthly_report")
