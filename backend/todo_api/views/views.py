from database import TODO_TABLE
from fastapi import APIRouter, HTTPException
from starlette.requests import Request
from tinydb import where
from todo_api.views.helpers import extract_username, get_user_from_db, crate_user, get_user_from_request, retrieve_todo
from todo_api.views.models import Login, User, PartialTodo, ReturnTodo

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
    new_todo = ReturnTodo(**todo.dict(), **partial_todo.dict())
    TODO_TABLE.update(doc_ids=[todo_id], **new_todo.dict())
    return new_todo


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
