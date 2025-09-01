from datetime import datetime
from pydantic import BaseModel, BeforeValidator, Field
from typing import Optional, Annotated


PyObjectId = Annotated[str, BeforeValidator(str)]

class TodoList(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    title: str
    description: str
    status: str
    priority: str
    due_date: Optional[datetime] = None

    class Config:
        populate_by_name =  True
        arbitrary_types_allowed = True