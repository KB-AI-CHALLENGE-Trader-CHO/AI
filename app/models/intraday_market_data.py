from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import DATETIME, DOUBLE, BIGINT
from .base import Base


class IntradayMarketData(Base):
    __tablename__ = "intraday_market_data"
    __table_args__ = (UniqueConstraint("stock_item_id", "intra_date_time", name="uk_stock_item_id_date"),)

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    stock_item_id = Column(BIGINT, ForeignKey("stock_item.id", ondelete="CASCADE"), nullable=False)
    intra_date_time = Column(DATETIME, nullable=False)
    open_price = Column(DOUBLE, nullable=True)
    high_price = Column(DOUBLE, nullable=True)
    low_price = Column(DOUBLE, nullable=True)
    close_price = Column(DOUBLE, nullable=True)
    volume = Column(BIGINT, nullable=True)
    ma_12_period = Column(DOUBLE, nullable=True)
    ma_20_period = Column(DOUBLE, nullable=True)
    rsi_14_period = Column(DOUBLE, nullable=True)
    bollinger_mid = Column(DOUBLE, nullable=True)
    bollinger_upper = Column(DOUBLE, nullable=True)
    bollinger_lower = Column(DOUBLE, nullable=True)
    atr_14_period = Column(DOUBLE, nullable=True)
    stochastic_k = Column(DOUBLE, nullable=True)
    stochastic_d = Column(DOUBLE, nullable=True)
    obv = Column(BIGINT, nullable=True)
    keltner_mid = Column(DOUBLE, nullable=True)
    keltner_upper = Column(DOUBLE, nullable=True)
    keltner_lower = Column(DOUBLE, nullable=True)

    # 관계 설정
    stock_item = relationship("StockItem", back_populates="intraday_market_datas", passive_deletes=True, uselist=False)
