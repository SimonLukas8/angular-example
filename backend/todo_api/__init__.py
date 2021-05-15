import views
from fastapi import FastAPI
from todo_api.middleware import AuthenticationMiddleware

app = FastAPI()

app.add_middleware(AuthenticationMiddleware)
app.include_router(views.router)
