from pydantic import ConfigDict
from typing import Optional
from fastapi_users import schemas
from pydantic.version import VERSION as PYDANTIC_VERSION


class UserRead(schemas.BaseUser[int]):
    username: str
    id: int
    email: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    if PYDANTIC_VERSION.startswith("2."):
        model_config = ConfigDict(from_attributes=True)
    else:

        class Config:
            from_attributes = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
