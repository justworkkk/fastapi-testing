from fastapi import APIRouter

router = APIRouter(prefix="/operations", tags=["Operation"])


@router.get("/")
async def test():
    return {"hello": "world"}
