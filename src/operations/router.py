from typing import Dict, List
from fastapi import APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from src.operations.models import operation
from src.operations.schemas import OperationCreate, ResponseModel
from src.database import get_async_session

router = APIRouter(prefix="/operations", tags=["Operation"])


@router.get("/", response_model=ResponseModel)
async def get_operations(
    currency: str, session: AsyncSession = Depends(get_async_session)
):
    query = select(operation).where(operation.c.currency == currency)
    result = await session.execute(query)
    return {"status": "success", "data": result.all(), "details": ""}


@router.post("/", response_model=ResponseModel)
async def add_operations(
    new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)
):
    stmt = insert(operation).values(**new_operation.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success", "data": [], "details": ""}
