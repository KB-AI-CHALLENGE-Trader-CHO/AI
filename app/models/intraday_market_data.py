from sqlalchemy import Column, BigInteger, ForeignKey, UniqueConstraint, Float
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import DATETIME
from .base import Base


class IntradayMarketData(Base):
    __tablename__ = "intraday_market_data"
    __table_args__ = (UniqueConstraint("stock_item_id", "intra_date_time", name="uk_stock_item_id_date"),)
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    stock_item_id = Column(BigInteger, ForeignKey("stock_item.id", ondelete="CASCADE"), nullable=False)
    intra_date_time = Column(DATETIME, nullable=False)
    open_price = Column(Float, nullable=True)
    high_price = Column(Float, nullable=True)
    low_price = Column(Float, nullable=True)
    close_price = Column(Float, nullable=True)
    volume = Column(BigInteger, nullable=True)
    ma_12_period = Column(Float, nullable=True)
    ma_20_period = Column(Float, nullable=True)
    rsi_14_period = Column(Float, nullable=True)
    bollinger_mid = Column(Float, nullable=True)
    bollinger_upper = Column(Float, nullable=True)
    bollinger_lower = Column(Float, nullable=True)
    atr_14_period = Column(Float, nullable=True)
    stochastic_k = Column(Float, nullable=True)
    stochastic_d = Column(Float, nullable=True)
    obv = Column(BigInteger, nullable=True)
    keltner_mid = Column(Float, nullable=True)
    keltner_upper = Column(Float, nullable=True)
    keltner_lower = Column(Float, nullable=True)

    # 관계 설정
    stock_item = relationship("StockItem", back_populates="intraday_market_data", passive_deletes=True)
