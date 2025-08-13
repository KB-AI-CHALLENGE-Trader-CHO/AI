from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import DATE, BIGINT, VARCHAR
from .base import Base


class MonthlyReport(Base):
    __tablename__ = "monthly_report"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    period = Column(DATE, nullable=False)
    summary = Column(VARCHAR(500), nullable=True)

    # 관계 설정
    monthly_analyses = relationship("MonthlyAnalysis", back_populates="monthly_report")
