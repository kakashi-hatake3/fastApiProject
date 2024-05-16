from fastapi import FastAPI, Depends
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_users import FastAPIUsers

from src.auth.base_config import auth_backend, current_user
from src.auth.manager import get_user_manager

from src.auth.models import User

from src.booking.router import router as booking_router
from src.tasks.router import router as tasks_router
from src.auth.router import router as auth_router

from redis import asyncio as aioredis

app = FastAPI()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.name}"


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

app.include_router(booking_router)
app.include_router(tasks_router)
app.include_router(auth_router)
