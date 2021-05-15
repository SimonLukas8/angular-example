import base64
import json

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

        return str(base64.encodebytes(bytes(f"{json.dumps(token_object)}", encoding="UTF_8")), encoding="UTF_8")


class ToDo(BaseModel):
    heading: str
    content: str
    user: str


class Login(BaseModel):
    username: str
    password: str
