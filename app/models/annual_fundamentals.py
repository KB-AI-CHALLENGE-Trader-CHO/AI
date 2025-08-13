from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, DECIMAL
from sqlalchemy.orm import relationship
from .base import Base


class AnnualFundamentals(Base):
    __tablename__ = "annual_fundamentals"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    stock_item_id = Column(BIGINT, ForeignKey("stock_item.id", ondelete="CASCADE"), nullable=False)
    period = Column(VARCHAR(4), nullable=False)
    per = Column(DECIMAL(10, 2), nullable=True)
    pbr = Column(DECIMAL(10, 2), nullable=True)
    roe = Column(DECIMAL(10, 2), nullable=True)
    dividend_yield = Column(DECIMAL(5, 2), nullable=True)
    ev_ebitda = Column(DECIMAL(10, 2), nullable=True)
    gross_profit_margin = Column(DECIMAL(10, 4), nullable=True)
    debt_to_equity = Column(DECIMAL(10, 4), nullable=True)

    # 관계 설정
    stock_items = relationship("StockItem", back_populates="annual_fundamental", passive_deletes=True)
