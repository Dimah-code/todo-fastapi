from fastapi import FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends

from .auth import authenticate_user, create_access_token, get_current_user
from . import models
from .schemas import TodoResponse, TodoCreate

from typing import List

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Todo app is running."}

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token({"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}



@app.get("/todos", response_model=List[TodoResponse])
def get_todos(user=Depends(get_current_user)):
    return models.todos_list()

@app.post("/todos", response_model=TodoResponse)
def create_todo(todo: TodoCreate, user=Depends(get_current_user)):
    return models.create_todo(todo)

