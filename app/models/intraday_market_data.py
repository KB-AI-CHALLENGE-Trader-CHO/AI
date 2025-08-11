from sqlalchemy import BigInteger, Column, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.mysql import BIGINT, DATETIME
from sqlalchemy.orm import relationship
from sqlalchemy.types import Numeric
from .base import Base


class IntradayMarketData(Base):
    __tablename__ = "intraday_market_data"
    __table_args__ = (UniqueConstraint("stock_item_id", "intra_date_time", name="uk_stock_item_id_date"),)

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    stock_item_id = Column(BigInteger, ForeignKey("stock_item.id", ondelete="CASCADE"), nullable=False)
    intra_date_time = Column(DATETIME, nullable=False)
    open_price = Column(Numeric(12, 2), nullable=True)
    high_price = Column(Numeric(12, 2), nullable=True)
    low_price = Column(Numeric(12, 2), nullable=True)
    close_price = Column(Numeric(12, 2), nullable=True)
    volume = Column(BIGINT(unsigned=False), nullable=True)
    ma_20d = Column(Numeric(12, 2), nullable=True)
    ma_50d = Column(Numeric(12, 2), nullable=True)
    ma_100d = Column(Numeric(12, 2), nullable=True)
    rsi_14d = Column(Numeric(10, 2), nullable=True)
    bollinger_mid = Column(Numeric(12, 2), nullable=True)
    bollinger_upper = Column(Numeric(12, 2), nullable=True)
    bollinger_lower = Column(Numeric(12, 2), nullable=True)
    atr_14_period = Column(Numeric(10, 2), nullable=True)
    stochastic_k = Column(Numeric(10, 2), nullable=True)
    stochastic_d = Column(Numeric(10, 2), nullable=True)
    obv = Column(BIGINT(unsigned=False), nullable=True)
    keltner_mid = Column(Numeric(12, 2), nullable=True)
    keltner_upper = Column(Numeric(12, 2), nullable=True)
    keltner_lower = Column(Numeric(12, 2), nullable=True)

    # 의존 관계 설정
    stock_item = relationship("StockItem", back_populates="intraday_market_data", passive_deletes=True)
