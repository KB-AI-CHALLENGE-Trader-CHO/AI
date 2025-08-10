from sqlalchemy import Column, String, Text, BigInteger
from sqlalchemy.dialects.mysql import DATETIME, ENUM
from app.database import Base


class Analysis(Base):
    __tablename__ = "analysis"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    date_time = Column(DATETIME(fsp=6), nullable=False)
    symbol = Column(String(20), nullable=False)
    stock_name = Column(String(100), nullable=False)
    memo = Column(String(255), nullable=True, default=None)
    analysis_details = Column(Text, nullable=True)
    suggestion = Column(Text, nullable=True)
    trade_type = Column(ENUM('BUY', 'SELL'), nullable=False)
