from fastapi import APIRouter, HTTPException
from schemas.todomodel import Todo, TodoUpdate
from database.database import collection
from bson import ObjectId

router = APIRouter()


@router.get("/todos/")
def get_todos():
    todos = []
    for todo in collection.find():
        todo["id"] = str(todo["_id"])
        del todo["_id"]
        todos.append(todo)
    return todos


@router.get("/todos/{id}")
def get_todo(id: str):
    todo = collection.find_one({"_id": ObjectId(id)})
    if todo:
        todo["id"] = str(todo["_id"])
        del todo["_id"]
        return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@router.post("/todos/")
def create_todo(todo: Todo):
    todo_dict = dict(todo)
    if "id" in todo_dict:
        del todo_dict["id"]
    result = collection.insert_one(todo_dict)
    new_todo = collection.find_one({"_id": result.inserted_id})
    new_todo["id"] = str(new_todo["_id"])
    del new_todo["_id"]
    return new_todo


@router.put("/todos/{id}")
def update_todo(id: str, todo: TodoUpdate):
    todo_dict = dict(todo)
    collection.update_one({"_id": ObjectId(id)}, {"$set": todo_dict})
    updated_todo = collection.find_one({"_id": ObjectId(id)})
    if updated_todo:
        updated_todo["id"] = str(updated_todo["_id"])
        del updated_todo["_id"]
        return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")


@router.delete("/todos/{id}")
def delete_todo(id: str):
    result = collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count > 0:
        return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")
