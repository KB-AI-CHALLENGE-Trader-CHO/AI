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


test_intraday_timing = IntradayTiming(
    datetime=datetime.fromisoformat("2025-07-01 23:45:00"),
    trend="uptrend",
    ma_stack="bullish",
    price_vs_ma={
        "close_gt_ma20": True,
        "close_gt_ma50": True,
        "close_gt_ma100": True
    },
    rsi14=58.92,
    rsi_status="normal",
    stochastic={"k": 55.86, "d": 51.92, "status": "normal"},
    bollinger={"mid": 210.51, "upper": 214.15, "lower": 206.87, "event": "inside"},
    atr14_period=0.72,
    atr_regime="high",
    keltner={"mid": 210.55, "upper": 212.0, "lower": 209.11, "event": "inside"},
    volume_z=0.59,
)
