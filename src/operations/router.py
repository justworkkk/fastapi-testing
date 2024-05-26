from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from src.operations.models import operation
from src.operations.schemas import OperationCreate, ResponseModel
from src.database import get_async_session
from fastapi_cache.decorator import cache
import time

router = APIRouter(prefix="/operations", tags=["Operations"])


@router.get("/", response_model=ResponseModel)
async def get_operations(
    currency: str, session: AsyncSession = Depends(get_async_session)
):
    try:
        query = select(operation).where(operation.c.currency == currency)
        result = await session.execute(query)
        return {"status": "success", "data": result.all(), "details": ""}
    except Exception as exception_type:
        raise HTTPException(
            status_code=500,
            detail={
                "status": "error",
                "data": [],
                "details": f"Exception: {exception_type}",
            },
        )


@router.post("/", response_model=ResponseModel)
async def add_operations(
    new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)
):
    try:
        stmt = insert(operation).values(**new_operation.model_dump())
        await session.execute(stmt)
        await session.commit()
        return {"status": "success", "data": [], "details": ""}
    except Exception as exception_type:
        raise HTTPException(
            status_code=500,
            detail={
                "status": "error",
                "data": [],
                "details": f"Exception: {exception_type}",
            },
        )


@router.get("/sleep")
@cache(expire=60)
def sleep_func():
    time.sleep(2)
    return {"cache": "test"}
