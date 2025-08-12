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
