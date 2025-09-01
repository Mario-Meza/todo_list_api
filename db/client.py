from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from fastapi import status, HTTPException
from dotenv import load_dotenv
import os
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
NAME_MONGO_COLLECTION = os.getenv("NAME_MONGO_COLLECTION", "todo_list")


# clase
class MongoDB:
    # Atributo para almacenar la instancia del cliente MongoDB
    client: MongoClient = None

# Objeto(instancia) de del cliente MongoDB
db = MongoDB()

def connect_to_mongodb():
    try:
        db.client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000
        )
        db.client.server_info()
        print("Connected to MongoDB")
    except ConnectionFailure as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Failed to connect to MongoDB: {e}"
        )

def close_mongodb():
    if db.client:
        db.client.close()
        print("Closed MongoDB")

def get_database():
    if db.client is None:
        raise RuntimeError("Connection to database is not available")
    return db.client.local

