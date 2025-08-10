from sqlalchemy import UniqueConstraint, BigInteger, String
from sqlalchemy.testing.schema import Column

from app.database import Base


class StockItem(Base):
    __tablename__ = "stock_item"
    __table_args__ = (
        UniqueConstraint('symbol', name='UKlii804qpa7ebjtnnq7m9h27fk'),
    )

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    symbol = Column(String(255), nullable=False)
