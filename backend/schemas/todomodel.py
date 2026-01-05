from pydantic import BaseModel
from typing import Optional


class Todo(BaseModel):
    id: Optional[str] = None
    title: str
    description: str
    deadline: str


class TodoUpdate(BaseModel):
    title: str
    description: str
    deadline: str