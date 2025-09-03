from db.schemas.list_todo_schema import schema_validate, todo_schema
from fastapi import APIRouter, HTTPException, status
from db.model.list_todo_model import TodoList
from db.client import get_database
from dotenv import load_dotenv
from bson import ObjectId
import os

load_dotenv()

# CONSTANTES
NAME_MONGO_COLLECTION = os.getenv("NAME_MONGO_COLLECTION")

router = APIRouter(
    prefix="/api/v1/todo",
    tags=["todolist"],
)

@router.get("/", response_model=list[dict])
def get_todo_list():
    # Creation instance databae connection
    db = get_database()
    # store the database name in the variable "collection"
    collection = db[NAME_MONGO_COLLECTION]
    # Obtenemos todos los to-do del "documento", los convertimos a una lista, esta se asigna a "todo_from_db"
    todo_from_db = list(collection.find())
    # Formats the data obtained with "schema_validate" and assigns it to "response_data"
    response_data = schema_validate(todo_from_db)
    # We return the formatted data
    return response_data

@router.get("/{id}")
def get_todo_by_id(id: str):
    """
    # Search a "todo_list" by "id"
    # Usamos la funcion "search_todo" para buscarlo por su "id", lo convertimos a un "ObjectId" para que lo entienda
      MongoDB.
    " We use the "search_todo" function to search for it by its "id", and we convert it to an "ObjectId" so MongoDb understand.
    :param id: id del "todo_do"
    :return: El "todo_do" encontrado | una 404 si no existe
    """
    todo_from_db = search_todo("_id", ObjectId(id))
    return todo_schema(todo_from_db)

@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_todo_list(to_do: TodoList) -> dict:
    # Creation instance databae connection
    db = get_database()
    # store the database name in the variable "collection"
    collection = db[NAME_MONGO_COLLECTION]
    # We convert the object "field" in a dictionary with "model_dump".
    todo_to_dict = to_do.model_dump(by_alias=True)
    # Remove _id of body if exist
    todo_to_dict.pop("_id", None)
    # We insert a new document into the collection and assign it to "add_a_collection"
    add_a_collection = collection.insert_one(todo_to_dict)
    # We search for the new inserted document by its "_id" and assign it to "new_todo"
    new_todo = collection.find_one({"_id": add_a_collection.inserted_id})
    # # We return the updated document formatted with our schema and validated with todoList model
    return todo_schema(new_todo)

@router.put("/{id}", response_model=dict)
def update_todo_list(id: str, to_do: TodoList):
    # creaction of instance to database
    db = get_database()
    # store the database name in the variable "collection"
    collection = db[NAME_MONGO_COLLECTION]
    # In the "collection" we look for the "_id" and  convert the str into an "ObjectId" so that mongodb understand it.
    existing_todo = collection.find_one({"_id": ObjectId(id)})
    # Verify if exist | Not found
    if not existing_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"TodoList with id {id} not found"
        )
    # Prepare document to update
    todo_to_dict = to_do.model_dump(by_alias=True, exclude_unset=True)
    # Remove _id of body if exist
    todo_to_dict.pop("_id", None)
    # Replace complete document
    update_document = collection.find_one_and_replace(
        {"_id": ObjectId(id)},
        todo_to_dict,
        return_document=True
    )
    # returns the formatted document.
    return todo_schema(update_document)

@router.patch("/{id}", response_model=dict)
def update_only_value(id: str, field: TodoList):
    # creaction of instance to database
    db = get_database()
    # store the database name in the variable "collection"
    collection = db[NAME_MONGO_COLLECTION]
    # Buscamos en la colección el documento por "_id"
    # Convertimos el string 'id' recibido a ObjectId para que MongoDB lo entienda
    update_result = collection.find_one({"_id": ObjectId(id)})
    # Verify if exist | Not found
    if not update_result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"TodoList with id {id} not found"
        )

    # We convert the object "field" in a dictionary with "model_dump".
    # - exclude_unset=True → Ignore fields that were not sent
    # - exclude_none=True → Ignore fields that come in as null.
    update_data = field.model_dump(exclude_unset=True, exclude_none=True)
    # If not exist
    if not update_data:
        raise  HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No field to update"
        )
    # We Updated only fileds that come in the request
    # - {"$set": update_data} → operador de MongoDB para actualizar campos específicos.
    update_document = collection.find_one_and_update(
        {"_id": ObjectId(id)},# Filter by id
        {"$set": update_data},# solo actualiza esos campos. Just update those fields
        return_document=True# Regresa el documento actualizado. Return the updated document
    )
    # We return the updated document formatted with our schema
    return todo_schema(update_document)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo_by_id(id: str):
    # We create instance to database
    db = get_database()
    # store the database name in the variable "collection"
    collection = db[NAME_MONGO_COLLECTION]
    # We found for by "_id" in the collection
    # We convert the received string to ObjectId so that MongoDb can understand it.
    found = collection.find_one_and_delete({"_id": ObjectId(id)})
    # if not exist
    if not found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"TodoList with id {id} not found"
        )
    return None

def search_todo(field: str, key):
    # We create an instance to the database
    db = get_database()
    # store the database name in the variable "collection"
    collection = db[NAME_MONGO_COLLECTION]
    # Search first document that match with (field) = valor (key)
    # Ejemplo: if field="titulo" y key="Estudiar FastAPI"
    # Mongo will do this: { "titulo": "Estudiar FastAPI" }
    todo_list = collection.find_one({field: key})
    # if no document is found throws an error
    if not todo_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found {field}"
        )
    # retorna un documento encontrado.
    return todo_list