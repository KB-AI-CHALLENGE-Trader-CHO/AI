from enum import Enum

from pydantic import BaseModel


class TradeType(str, Enum):
    BUY = "BUY"
    SELL = "SELL"


class PriceVsMA(BaseModel):
    close_gt_ma20: bool
    close_gt_ma50: bool
    close_gt_ma100: bool


class Stochastic(BaseModel):
    k: float
    d: float
    status: str


class Bollinger(BaseModel):
    mid: float
    upper: float
    lower: float
    event: str


class Keltner(BaseModel):
    mid: float
    upper: float
    lower: float
    event: str
