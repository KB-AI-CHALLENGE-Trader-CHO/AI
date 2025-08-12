from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel

from app.schemas.common_schema import PriceVsMA, Stochastic, Bollinger, Keltner


class IntradayTiming(BaseModel):
    datetime: datetime
    trend: str
    ma_stack: str
    price_vs_ma: PriceVsMA
    rsi14: float
    rsi_status: str
    stochastic: Stochastic
    bollinger: Bollinger
    atr14_period: float
    atr_regime: str
    keltner: Keltner
    volume_z: float
