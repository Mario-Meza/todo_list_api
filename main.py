from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers import to_do_list
from db.client import connect_to_mongodb, close_mongodb

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:4321",  # El puerto por defecto de Astro dev server
    # Agrega aquí otras URLs si es necesario
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los headers
)

app.include_router(to_do_list.router)
app.add_event_handler("startup", connect_to_mongodb)
app.add_event_handler("shutdown", close_mongodb)

@app.get("/")
async def root():
    return {"message": "Hello World"}
