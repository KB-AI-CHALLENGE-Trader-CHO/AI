from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import DATETIME, LONGTEXT, BIGINT
from sqlalchemy.orm import relationship
from .base import Base


class WeeklyAnalysis(Base):
    __tablename__ = "weekly_analysis"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    analysis_details = Column(LONGTEXT)
    date_time = Column(DATETIME(fsp=6), nullable=False)
    suggestion = Column(LONGTEXT)
    history_id = Column(BIGINT, ForeignKey("trade_history.id"), nullable=False)
    weekly_report_id = Column(BIGINT, ForeignKey("weekly_report.id"))

    # 관계 설정
    weekly_report = relationship("WeeklyReport", back_populates="weekly_analyses", uselist=False)
    trade_history = relationship("TradeHistory", back_populates="weekly_analysis", uselist=False)
