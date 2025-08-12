from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import relationship
from .base import Base


class WeeklyAnalysis(Base):
    __tablename__ = "weekly_analysis"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    weekly_report_id = Column(BigInteger, ForeignKey("weekly_report.id"))
    history_id = Column(BigInteger, ForeignKey("trade_history.id"), nullable=False)
    date_time = Column(DATETIME(fsp=6), nullable=False)
    analysis_details = Column(mysql.TINYTEXT)
    suggestion = Column(mysql.LONGTEXT)

    # 관계 설정
    weekly_report = relationship("WeeklyReport", back_populates="weekly_analyses")
    trade_history = relationship("TradeHistory", back_populates="weekly_analysis")
