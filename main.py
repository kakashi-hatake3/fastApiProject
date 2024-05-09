from datetime import datetime
from enum import Enum
from typing import List, Optional
from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers
from pydantic import BaseModel, Field

from auth.auth import auth_backend
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate

from auth.database import User

app = FastAPI()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.name}"


#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}!!!"}
#
#
# users_list = [
#     {"id": 0, "name": "Ivan", "role": "loser"},
#     {"id": 1, "name": "Dima", "role": "admin"},
#     {"id": 2, "name": "Bogdan", "role": "goat"},
#     {"id": 3, "name": "Vasya", "role": "lox", "degree": [{
#         "id": 0, "created_at": "2024-05-05T13:03:07", "type_degree": "newbie"
#     }]}
#               ]
#
#
# class DegreeType(Enum):
#     newbie = "newbie"
#     expert = "expert"
#     lox = "lox"
#
#
# class Degree(BaseModel):
#     id: int
#     created_at: datetime
#     type_degree: DegreeType
#
#
# class User(BaseModel):
#     id: int
#     name: str
#     role: str
#     degree: Optional[List[Degree]] = []
#
#
# @app.get("/users/{user_id}", response_model=List[User])
# def get_users(user_id: int = 1):
#     return [user for user in users_list if user.get("id") == user_id]
#
#
# users_actions = [
#     {"id": 0, "action": "nothing"},
#     {"id": 1, "action": "coding"},
#     {"id": 2, "action": "reading"},
#     {"id": 3, "action": "fapping"},
#     {"id": 4, "action": "sleeping"},
#     {"id": 5, "action": "sitting"},
#     {"id": 6, "action": "raising"},
#     {"id": 7, "action": "crawling"},
#     {"id": 8, "action": "singing"},
#     {"id": 9, "action": "testing"},
#     {"id": 10, "action": "github"}
#               ]
#
#
# @app.get("/actions")
# def get_actions(count: int = 3, starts_w: int = 0):
#     return users_actions[starts_w:][:count]
#
#
# @app.get("/gay")
# def get_gay():
#     return "gay shit"
#
#
# @app.post("/users/{user_id}")
# def rename(user_id: int, new_name: str):
#     current_user = list(filter(lambda user: user.get("id") == user_id, users_list))[0]
#     current_user["name"] = new_name
#     return {"status": 200, "data": current_user}
#
#
# class Action(BaseModel):
#     id: int
#     action: str = Field(max_length=7)
#
#
# @app.post("/actions")
# def add_actions(new_actions: List[Action]):
#     users_actions.extend(new_actions)
#     return {"status": 200, "data": users_actions}
