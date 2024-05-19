from typing import Dict, List
from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()


class User(BaseModel):
    username: str = Field(max_length=20)
    email: str


users: List[User] = []


@app.get("/test")
def test(username: str, email: str):
    content = {"status": 200, "username": username, "email": email}
    return content


@app.post("/user", response_model=List[User])
def user_post(user_post: User):
    global users
    users.append(user_post)
    return users
