from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import DATETIME, BIGINT, LONGTEXT
from sqlalchemy.orm import relationship
from .base import Base


class MonthlyAnalysis(Base):
    __tablename__ = "monthly_analysis"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    analysis_details = Column(LONGTEXT)
    date_time = Column(DATETIME(fsp=6), nullable=False)
    suggestion = Column(LONGTEXT)
    monthly_report_id = Column(BIGINT, ForeignKey("monthly_report.id"))
    stock_item_id = Column(BIGINT, ForeignKey("stock_item.id"))

    # 관계 설정
    monthly_report = relationship("MonthlyReport", back_populates="monthly_analyses", uselist=False)
    stock_item = relationship("StockItem", back_populates="monthly_analyses", uselist=False)
