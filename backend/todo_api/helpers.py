import base64
import json
from typing import Dict, Optional

from database import USER_TABLE
from models import User
from starlette.requests import Request
from tinydb import Query


def extract_username(request: Request) -> str:
    user = decode_user_dict(request)
    return user["username"]


def decode_user_dict(request: Request) -> Dict[str, str]:
    header = request.headers.get("authorization")
    decoded_header = base64.decodebytes(bytes(header, encoding="UTF_8"))
    return json.loads(decoded_header)


def generate_token(username: str, password: str) -> str:
    return User.generate_token(username, password)


def get_user_from_db(username: str) -> Optional[User]:
    user_query = Query()
    db_user = USER_TABLE.search(user_query.username == username)

    if not db_user:
        return None

    db_user = db_user[0]

    return User(username=username, token=db_user["token"], id=db_user.doc_id)


def crate_user(username: str, password: str) -> User:
    token = generate_token(username, password)
    USER_TABLE.insert({"username": username, "token": token})
    return get_user_from_db(username)
