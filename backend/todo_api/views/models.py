import base64
import json
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    username: str
    token: str
    id: int

    def password_valid(self, password: str) -> bool:
        token = User.generate_token(self.username, password)
        return token == self.token

    @staticmethod
    def generate_token(username: str, password: str) -> str:
        token_object = {
            "username": username,
            "password": password
        }
        token_str = bytes(f"{json.dumps(token_object)}", encoding="UTF_8")

        return str(base64.encodebytes(token_str), encoding="UTF_8") \
            .replace("\\n", "")


class PartialTodo(BaseModel):
    heading: Optional[str]
    content: Optional[str]


class PostTodo(BaseModel):
    heading: str
    content: str


class ToDo(PostTodo):
    time: float
    user_id: int


class ReturnTodo(ToDo):
    id: int


class Login(BaseModel):
    username: str
    password: str
