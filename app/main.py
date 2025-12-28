from fastapi import FastAPI

from . import models
from .schemas import TodoResponse, TodoCreate


from typing import List

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Todo app is running."}


@app.get("/todos", response_model=List[TodoResponse], tags=["Todos"])
def get_todos():
    return models.todos_list()
