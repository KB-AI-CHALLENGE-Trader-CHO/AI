from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.dialects import mysql
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import relationship
from .base import Base


class MonthlyAnalysis(Base):
    __tablename__ = "monthly_analysis"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    monthly_report_id = Column(BigInteger, ForeignKey("monthly_report.id"), nullable=False)
    stock_item_id = Column(BigInteger, ForeignKey("stock_item.id"), nullable=False)
    date_time = Column(DATETIME(fsp=6), nullable=False)
    analysis_details = Column(mysql.TINYTEXT)
    suggestion = Column(mysql.LONGTEXT)

    # 의존 관계 설정
    monthly_report = relationship("MonthlyReport", back_populates="monthly_analyses")
    stock_item = relationship("StockItem", back_populates="monthly_analyses")
