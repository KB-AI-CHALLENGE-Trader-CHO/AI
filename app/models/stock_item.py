from sqlalchemy import Column
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR
from sqlalchemy.orm import relationship
from .base import Base


class StockItem(Base):
    __tablename__ = "stock_item"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255), nullable=False)
    symbol = Column(VARCHAR(255), nullable=False, unique=True)

    # 관계 설정
    trade_histories = relationship("TradeHistory", back_populates="stock_item")
    monthly_analyses = relationship("MonthlyAnalysis", back_populates="stock_item", passive_deletes=True)
    annual_fundamental = relationship("AnnualFundamentals", back_populates="stock_items", passive_deletes=True,
                                      uselist=False)
    daily_market_datas = relationship("DailyMarketData", back_populates="stock_item", passive_deletes=True)
    intraday_market_datas = relationship("IntradayMarketData", back_populates="stock_item", passive_deletes=True)
