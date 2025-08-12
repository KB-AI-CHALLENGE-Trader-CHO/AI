from enum import Enum
from sqlalchemy import BigInteger, Column, Enum as SAEnum, ForeignKey, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import TIME, DATE
from .base import Base


class TradeType(str, Enum):
    BUY = "BUY"
    SELL = "SELL"


class TradeHistory(Base):
    __tablename__ = "trade_history"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    stock_item_id = Column(BigInteger, ForeignKey("stock_item.id"), nullable=False)
    avg_buy_price = Column(Float, nullable=True)
    price = Column(Float, nullable=False)
    quantity = Column(Float, nullable=False)
    trade_date = Column(DATE, nullable=False)
    trade_time = Column(TIME(fsp=6), nullable=False)
    memo = Column(String(255), nullable=True)
    trade_type = Column(SAEnum(TradeType, name="trade_type", native_enum=False), nullable=False)

    # 관계 설정
    stock_item = relationship("StockItem", back_populates="trade_histories")
    weekly_analysis = relationship("WeeklyAnalysis", back_populates="trade_history", uselist=False)
    trade_evaluation = relationship("TradeEvaluation", back_populates="trade_history", cascade="all, delete-orphan",
                                     lazy="selectin")

    def to_dict(self) -> dict:
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
