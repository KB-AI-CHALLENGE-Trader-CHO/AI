from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import ENUM, TIMESTAMP, BIGINT, DECIMAL, INTEGER
from sqlalchemy.orm import relationship
from .base import Base


class TradeEvaluation(Base):
    __tablename__ = "trade_evaluation"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    daily_atr_regime = Column(ENUM("high", "low", "mid", "unknown"), nullable=True)
    daily_bb_event = Column(ENUM("break_lower", "break_upper", "inside", "touch_lower", "touch_upper", "unknown"),
                            nullable=True)
    daily_keltner_event = Column(ENUM("break_lower", "break_upper", "inside", "touch_lower", "touch_upper", "unknown"),
                                 nullable=True)
    daily_ma_stack = Column(ENUM("bearish", "bullish", "mixed"), nullable=True)
    daily_obv_signal = Column(ENUM("bearish", "bullish", "none"), nullable=True)
    daily_rsi = Column(DECIMAL(10, 2), nullable=True)
    daily_rsi_status = Column(ENUM("normal", "overbought", "oversold", "unknown"), nullable=True)
    daily_stoch_k = Column(DECIMAL(10, 2), nullable=True)
    daily_stoch_status = Column(ENUM("normal", "overbought", "oversold", "unknown"), nullable=True)
    daily_trend = Column(ENUM("downtrend", "sideways", "uptrend"), nullable=True)
    evaluated_at = Column(TIMESTAMP, nullable=True)
    intra_bb_event = Column(ENUM("break_lower", "break_upper", "inside", "touch_lower", "touch_upper", "unknown"),
                            nullable=True)
    intra_keltner_event = Column(ENUM("break_lower", "break_upper", "inside", "touch_lower", "touch_upper", "unknown"),
                                 nullable=True)
    intra_ma_stack = Column(ENUM("bearish", "bullish", "mixed"), nullable=True)
    intra_rsi = Column(DECIMAL(10, 2), nullable=True)
    intra_rsi_status = Column(ENUM("normal", "overbought", "oversold", "unknown"), nullable=True)
    intra_stoch_k = Column(DECIMAL(10, 2), nullable=True)
    intra_stoch_status = Column(ENUM("normal", "overbought", "oversold", "unknown"), nullable=True)
    intra_trend = Column(ENUM("downtrend", "sideways", "uptrend"), nullable=True)
    intra_volume_z = Column(DECIMAL(10, 2), nullable=True)
    score_confidence = Column(DECIMAL(4, 2), nullable=True)
    score_context = Column(INTEGER, nullable=True)
    score_rationale = Column(INTEGER, nullable=True)
    score_risk = Column(INTEGER, nullable=True)
    score_timing = Column(INTEGER, nullable=True)
    score_total = Column(INTEGER, nullable=True)
    trade_history_id = Column(BIGINT, ForeignKey("trade_history.id"), nullable=False)

    # 관계 설정
    trade_history = relationship("TradeHistory", back_populates="trade_evaluation", uselist=False)

    def to_dict(self) -> dict:
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
