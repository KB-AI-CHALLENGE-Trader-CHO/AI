from sqlalchemy import BigInteger, Column, String
from sqlalchemy.orm import relationship
from .base import Base


class StockItem(Base):
    __tablename__ = "stock_item"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    symbol = Column(String(255), nullable=False, unique=True)

    # 의존 관계 설정
    trade_histories = relationship("TradeHistory", back_populates="stock_item")
    monthly_analyses = relationship("MonthlyAnalysis", back_populates="stock_item", passive_deletes=True)
    weekly_analyses = relationship("WeeklyAnalysis", back_populates="stock_item", passive_deletes=True)
    annual_fundamentals = relationship("AnnualFundamentals", back_populates="stock_item", passive_deletes=True)
    daily_market_data = relationship("DailyMarketData", back_populates="stock_item", passive_deletes=True)
    intraday_market_data = relationship("IntradayMarketData", back_populates="stock_item", passive_deletes=True)
