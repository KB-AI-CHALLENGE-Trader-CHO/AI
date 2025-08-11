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


test_daily_context = DailyContext(
    date=date.fromisoformat("2025-07-01"),
    trend="sideways",
    ma_stack="mixed",
    price_vs_ma={
        "close_gt_ma20": True,
        "close_gt_ma50": True,
        "close_gt_ma100": False
    },
    rsi14=59.36,
    rsi_status="normal",
    stochastic={"k": 84.33, "d": 73.76, "status": "overbought"},
    bollinger={"mid": 200.96, "upper": 206.93, "lower": 195.0, "event": "break_upper"},
    atr14=3.97,
    atr_regime="low",
    obv=2024919473.0,
    obv_signal="none",
    keltner={"mid": 201.75, "upper": 209.7, "lower": 193.8, "event": "inside"},
)
