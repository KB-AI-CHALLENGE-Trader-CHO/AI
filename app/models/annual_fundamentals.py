from sqlalchemy import BigInteger, Column, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.types import Numeric
from .base import Base


class AnnualFundamentals(Base):
    __tablename__ = "annual_fundamentals"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    stock_item_id = Column(BigInteger, ForeignKey("stock_item.id", ondelete="CASCADE"), nullable=False)
    period = Column(String(4), nullable=False)
    per = Column(Numeric(10, 2), nullable=True)
    pbr = Column(Numeric(10, 2), nullable=True)
    roe = Column(Numeric(10, 2), nullable=True)
    dividend_yield = Column(Numeric(5, 2), nullable=True)
    ev_ebitda = Column(Numeric(10, 2), nullable=True)
    gross_profit_margin = Column(Numeric(10, 4), nullable=True)
    debt_to_equity = Column(Numeric(10, 4), nullable=True)

    # 의존 관계 설정
    stock_item = relationship("StockItem", back_populates="annual_fundamentals", passive_deletes=True)
