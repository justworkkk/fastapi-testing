from src.config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT_TEST, DB_USER
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from src.database import metadata
from typing import AsyncGenerator
from src.main import app
from src.database import get_async_session


# CONFIG IS NOT READY TO START TESTS!!!

DATABASE_URL_TEST = (
    f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT_TEST}/{DB_NAME}"
)

engine_test = create_async_engine(DATABASE_URL_TEST)
async_session_maker = async_sessionmaker(engine_test, expire_on_commit=False)
metadata.bind = engine_test


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


app.dependency_overrides[get_async_session] = override_get_async_session
