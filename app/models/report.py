from sqlalchemy import Column, BigInteger, Date, String

from app.database import Base


class WeeklyReport(Base):
    __tablename__ = "weekly_report"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    period = Column(Date, nullable=False)
    summary = Column(String(500), nullable=True, default=None)


class MonthlyReport(Base):
    __tablename__ = "monthly_report"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    period = Column(Date, nullable=False)
    summary = Column(String(500), nullable=True, default=None)
