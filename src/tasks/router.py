from fastapi import APIRouter, BackgroundTasks, Depends
from src.auth.auth_back import current_user
from src.operations.schemas import ResponseModel
from src.tasks.tasks import send_email
from src.database import User
import logging

log = logging.getLogger(__name__)


router = APIRouter(prefix="/report", tags=["Report"])


@router.get("/message", response_model=ResponseModel)
async def protect_route(user: User = Depends(current_user)):
    send_email.delay(user.username)
    log.info("Succesful sent message")
    return {"status": "success", "data": [], "details": "Message have sent"}
