from fastapi import APIRouter, Depends

from src.auth.base_config import current_user
from src.tasks.tasks import background_func

router = APIRouter(
    prefix="/background_task",
)


@router.get("/")
def get_background_task(user=Depends(current_user)):
    background_func(user.name)
    return {
        "status": "success",
        "detail": None,
    }
