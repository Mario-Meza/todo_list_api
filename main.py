from fastapi import FastAPI
from routers import to_do_list
from db.client import connect_to_mongodb, close_mongodb

app = FastAPI()
app.include_router(to_do_list.router)
app.add_event_handler("startup", connect_to_mongodb)
app.add_event_handler("shutdown", close_mongodb)

@app.get("/")
async def root():
    return {"message": "Hello World"}
