from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

# MySQL 엔진 생성
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    future=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)
