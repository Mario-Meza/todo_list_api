import os
from db.model.list_todo_model import TodoList
from bson import ObjectId
from fastapi import APIRouter, HTTPException, status
from dotenv import load_dotenv
from db.client import get_database
from db.schemas.list_todo_schema import schema_validate, todo_schema
load_dotenv()

# CONSTANTES
NAME_MONGO_COLLECTION = os.getenv("NAME_MONGO_COLLECTION")

router = APIRouter(
    prefix="/api/v1/todo",
    tags=["todolist"],
)

@router.get("/", response_model=list[dict])
def get_todo_list():
    db = get_database()
    todo_from_db = list(db[NAME_MONGO_COLLECTION].find())
    response_data = schema_validate(todo_from_db)

    return response_data

@router.get("/{id}")
def get_todo_list(id: str):
    todo_from_db = search_todo("_id", ObjectId(id))
    return todo_schema(todo_from_db)

@router.post("/", response_model=dict)
def create_todo_list(to_do: TodoList):
    db = get_database()
    todo_to_dict = to_do.model_dump(by_alias=True)
    todo_to_dict.pop("_id", None)
    add_a_collection = db[NAME_MONGO_COLLECTION].insert_one(todo_to_dict)
    new_todo = db[NAME_MONGO_COLLECTION].find_one({"_id": add_a_collection.inserted_id})

    return todo_schema(new_todo)



def search_todo(field: str, key):
    db = get_database()
    todo_list = db[NAME_MONGO_COLLECTION].find_one({field: key})
    if not todo_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found {field}"
        )
    return todo_list






