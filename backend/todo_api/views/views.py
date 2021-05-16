import time

from database import TODO_TABLE
from fastapi import APIRouter, HTTPException
from starlette.requests import Request
from tinydb import where
from todo_api.views.helpers import extract_username, get_user_from_db, crate_user, get_user_from_request, retrieve_todo
from todo_api.views.models import Login, User, PartialTodo, ReturnTodo, PostTodo, ToDo

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


@router.get("/todo/{todo_id}")
async def get_todo(todo_id: int, request: Request) -> ReturnTodo:
    todo_db = TODO_TABLE.get(todo_id)
    user = get_user_from_request(request)

    if not todo_db:
        raise HTTPException(404, "Item not found")

    todo = ReturnTodo(**todo_db)

    # Normally you should not admit, that the to-do exists, but...
    if todo.user_id != user.id:
        raise HTTPException(403, "You don't have access to this item")

    return todo


@router.patch("/todo/{todo_id}")
async def update_todo(todo_id: int, partial_todo: PartialTodo, request: Request) -> ReturnTodo:
    todo = retrieve_todo(todo_id, request)
    todo.merge_in(partial_todo)
    todo_dict = todo.dict()
    del todo_dict["id"]
    TODO_TABLE.update(todo_dict, doc_ids=[todo_id])
    return todo


@router.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int, request: Request) -> None:
    retrieve_todo(todo_id, request)
    TODO_TABLE.remove(doc_ids=[todo_id])


# TODO order, pagination
@router.get("/todo")
async def get_todos(request: Request) -> ReturnTodo:
    user = get_user_from_request(request)
    todo_items = TODO_TABLE.search(where("user_id") == user.id)
    for todo in todo_items:
        todo["id"] = todo.doc_id
    return todo_items


@router.post("/todo")
async def create_todo(post_todo: PostTodo, request: Request) -> ReturnTodo:
    user = get_user_from_request(request)
    todo = ToDo(**post_todo.dict(), time=time.time(), user_id=user.id)
    todo_id = TODO_TABLE.insert(todo.dict())
    return ReturnTodo(**todo.dict(), id=todo_id)
