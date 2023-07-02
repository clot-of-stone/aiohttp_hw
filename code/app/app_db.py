from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

PG_DSN = 'postgresql+asyncpg://postgres:postgres@postgredb'

engine = create_async_engine(PG_DSN)

Session = sessionmaker(bind=engine, class_=AsyncSession,
                       expire_on_commit=False)
