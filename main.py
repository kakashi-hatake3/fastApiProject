from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}!!!"}


users_list = [
    {"id": 0, "name": "Ivan", "role": "loser"},
    {"id": 1, "name": "Dima", "role": "admin"},
    {"id": 2, "name": "Bogdan", "role": "goat"}
              ]


@app.get("/users/{user_id}")
def get_users(user_id: int = 1):
    return [user for user in users_list if user.get("id") == user_id]


users_actions = [
    {"id": 0, "action": "nothing"},
    {"id": 1, "action": "coding"},
    {"id": 2, "action": "reading"},
    {"id": 3, "action": "fapping"},
    {"id": 4, "action": "sleeping"},
    {"id": 5, "action": "sitting"},
    {"id": 6, "action": "raising"},
    {"id": 7, "action": "crawling"},
    {"id": 8, "action": "singing"},
    {"id": 9, "action": "testing"},
    {"id": 10, "action": "github"}
              ]


@app.get("/actions")
def get_actions(count: int = 3, starts_w: int = 0):
    return users_actions[starts_w:][:count]
