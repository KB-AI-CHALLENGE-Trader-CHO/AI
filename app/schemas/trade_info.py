from __future__ import annotations

from datetime import datetime
from math import isnan
from typing import Optional

from pydantic import BaseModel, Field, field_validator

from app.schemas.common_schema import TradeType


class TradeInfo(BaseModel):
    id: int
    stock_item_id: int
    trade_type: TradeType
    trade_datetime: datetime
    price: float
    quantity: float
    avg_buy_price: Optional[float] = Field(default=None)
    memo: Optional[str] = None

    @field_validator("avg_buy_price", mode="before")
    @classmethod
    def _nan_to_none(cls, v):
        try:
            if v is not None and isinstance(v, float) and isnan(v):
                return None
        except Exception:
            pass
        return v


test_trade_info = TradeInfo(
    id=1,
    stock_item_id=2,
    trade_type="BUY",
    trade_datetime=datetime.fromisoformat("2025-07-01 23:47:00"),
    price=211.1,
    quantity=3.0,
    avg_buy_price="nan",
    memo="애플 가격 오른다고 해서 일단 샀다."
)
