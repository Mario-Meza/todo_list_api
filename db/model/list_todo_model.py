from datetime import datetime
from pydantic import BaseModel, BeforeValidator, Field
from typing import Optional, Annotated, Literal


PyObjectId = Annotated[str, BeforeValidator(str)]

class TodoList(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    title: str = Field(min_length=1)  # Obligatorio
    description: Optional[str] = Field(default="")  # Opcional con valor por defecto
    status: str = Field(default="pending")  # Con valor por defecto
    priority: str = Field(default="medium")  # Con valor por defecto
    due_date: Optional[datetime] = Field(default=None)  # Opcional

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True