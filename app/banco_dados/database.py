from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://projetotopazdb_user:afQIrRG6VfFUt0G5cgSKYrwXsJPJaFlP@dpg-cprpbgaj1k6c738cbtk0-a.oregon-postgres.render.com/projetotopazdb"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(
    bind=engine,
    class_= AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base()