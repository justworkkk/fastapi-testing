from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from src.auth.auth_back import auth_backend
from src.auth.manager import get_user_manager
from src.auth.schemas import UserRead, UserCreate
from src.database import User
from src.operations.router import router as router_operation
from src.tasks.router import router as router_tasks
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi.middleware.cors import CORSMiddleware
from src.pages.router import router as router_pages
from src.chat.router import router as router_chat
import sentry_sdk
import logging


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


app = FastAPI(lifespan=lifespan)

logging.basicConfig(level=logging.INFO)


console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

console_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
console_handler.setFormatter(console_formatter)

log = logging.getLogger(__name__)
log.addHandler(console_handler)


sentry_sdk.init(
    dsn="https://032dd9a8b14a14dfba4fae353ced280b@o4507125847621632.ingest.de.sentry.io/4507323943485520",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


# If you need cors middleware, you can uncomment code further

# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(router_operation)

app.include_router(router_tasks)

app.include_router(router_pages)

app.include_router(router_chat)
