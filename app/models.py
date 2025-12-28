from typing import List

from .schemas import TodoResponse, TodoCreate

TODOS: List[TodoResponse] = []
_counter = 0


def create_todo(data: TodoCreate) -> TodoResponse:
    global _counter
    _counter += 1

    todo = TodoResponse(id=_counter, **data.dict())
    TODOS.append(todo)
    return todo


def todos_list():
    return TODOS
