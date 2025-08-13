from enum import Enum
from sqlalchemy import Column, Enum as DBEnum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import TIME, DATE, BIGINT, VARCHAR, DOUBLE
from .base import Base


class TradeType(str, Enum):
    BUY = "BUY"
    SELL = "SELL"


class TradeHistory(Base):
    __tablename__ = "trade_history"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    avg_buy_price = Column(DOUBLE, nullable=True)
    trade_date = Column(DATE, nullable=False)
    memo = Column(VARCHAR(255), nullable=True)
    price = Column(DOUBLE, nullable=False)
    quantity = Column(DOUBLE, nullable=False)
    trade_time = Column(TIME(fsp=6), nullable=False)
    trade_type = Column(DBEnum(TradeType, name="trade_type", native_enum=False), nullable=False)
    stock_item_id = Column(BIGINT, ForeignKey("stock_item.id"), nullable=False)

    # 관계 설정
    stock_item = relationship("StockItem", back_populates="trade_histories", uselist=False)
    weekly_analysis = relationship("WeeklyAnalysis", back_populates="trade_history", uselist=False)
    trade_evaluation = relationship("TradeEvaluation", back_populates="trade_history", cascade="all, delete-orphan",
                                    uselist=False)

    def to_dict(self) -> dict:
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
