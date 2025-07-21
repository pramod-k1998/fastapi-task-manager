from fastapi import FastAPI
from . import models
from .database import engine
from .routers import users, tasks
from app.routers import users, tasks


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Task Manager"}