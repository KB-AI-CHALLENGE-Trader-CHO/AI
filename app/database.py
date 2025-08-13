from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

# MySQL 엔진 생성
engine = create_engine(
    url=settings.DATABASE_URL,
    echo=settings.DATABASE_SHOW_SQL_LOG,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True
)

# 글로벌 세션 설정
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)
