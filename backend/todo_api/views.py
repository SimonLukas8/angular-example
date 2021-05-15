from fastapi import APIRouter, HTTPException
from helpers import extract_username, get_user_from_db, crate_user
from models import Login, User
from starlette.requests import Request

router = APIRouter()


@router.post("/login", response_model=User)
async def login(login_form: Login):
    user = get_user_from_db(login_form.username)

    if not user:
        user = crate_user(login_form.username, login_form.password)

    if not user.password_valid(login_form.password):
        raise HTTPException(400, "Password wrong")

    return user


@router.get("/account")
async def login(request: Request):
    username = extract_username(request)

    return get_user_from_db(username)
