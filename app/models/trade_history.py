from sqlalchemy import Column, BigInteger, Date, String
from sqlalchemy.dialects.mysql import DOUBLE, ENUM, TIME

from app.database import Base


class TradeHistory(Base):
    __tablename__ = "trade_history"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    avg_buy_price = Column(DOUBLE, nullable=True)
    price = Column(DOUBLE, nullable=False)
    quantity = Column(DOUBLE, nullable=False)
    trade_date = Column(Date, nullable=False)
    trade_time = Column(TIME(fsp=6), nullable=False)
    memo = Column(String(255), nullable=True, default=None)
    name = Column(String(255), nullable=False)
    symbol = Column(String(255), nullable=False)
    trade_type = Column(ENUM('BUY', 'SELL'), nullable=False)
