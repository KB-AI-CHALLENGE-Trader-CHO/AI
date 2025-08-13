from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.mysql import BIGINT, DATE, DOUBLE
from sqlalchemy.orm import relationship

from .base import Base


class DailyMarketData(Base):
    __tablename__ = "daily_market_data"
    __table_args__ = (UniqueConstraint("stock_item_id", "daily_date", name="uk_stock_item_id_date"),)

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    stock_item_id = Column(BIGINT, ForeignKey("stock_item.id", ondelete="CASCADE"), nullable=False)
    daily_date = Column(DATE, nullable=False)
    open_price = Column(DOUBLE, nullable=True)
    high_price = Column(DOUBLE, nullable=True)
    low_price = Column(DOUBLE, nullable=True)
    close_price = Column(DOUBLE, nullable=True)
    volume = Column(BIGINT(unsigned=False), nullable=True)
    ma_20d = Column(DOUBLE, nullable=True)
    ma_50d = Column(DOUBLE, nullable=True)
    ma_100d = Column(DOUBLE, nullable=True)
    rsi_14d = Column(DOUBLE, nullable=True)
    bollinger_mid = Column(DOUBLE, nullable=True)
    bollinger_upper = Column(DOUBLE, nullable=True)
    bollinger_lower = Column(DOUBLE, nullable=True)
    atr_14d = Column(DOUBLE, nullable=True)
    stochastic_k = Column(DOUBLE, nullable=True)
    stochastic_d = Column(DOUBLE, nullable=True)
    obv = Column(BIGINT(unsigned=False), nullable=True)
    keltner_mid = Column(DOUBLE, nullable=True)
    keltner_upper = Column(DOUBLE, nullable=True)
    keltner_lower = Column(DOUBLE, nullable=True)

    # 관계 설정
    stock_item = relationship("StockItem", back_populates="daily_market_datas", passive_deletes=True, uselist=False)
