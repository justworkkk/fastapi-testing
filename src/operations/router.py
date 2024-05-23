from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from src.operations.models import operation
from src.operations.schemas import OperationCreate
from src.database import get_async_session

router = APIRouter(prefix="/operations", tags=["Operation"])


@router.get("/", response_model=List[OperationCreate])
async def get_operations(session: AsyncSession = Depends(get_async_session)):
    query = select(operation)
    result = await session.execute(query)
    return result.all()


@router.post("/")
async def add_operations(
    new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)
):
    stmt = insert(operation).values(**new_operation.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {"status": "successful"}
