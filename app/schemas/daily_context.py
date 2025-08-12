from __future__ import annotations

from datetime import date

from pydantic import BaseModel

from app.schemas.common_schema import PriceVsMA, Stochastic, Bollinger, Keltner


class DailyContext(BaseModel):
    date: date
    trend: str
    ma_stack: str
    price_vs_ma: PriceVsMA
    rsi14: float
    rsi_status: str
    stochastic: Stochastic
    bollinger: Bollinger
    atr14: float
    atr_regime: str
    obv: float
    obv_signal: str
    keltner: Keltner
