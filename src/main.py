from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from src.auth.auth_back import auth_backend
from src.auth.manager import get_user_manager
from src.auth.schemas import UserRead, UserCreate
from src.database import User
from src.operations.router import router as router_operation

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI()


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    # prefix="/auth/jwt",
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(router_operation)
