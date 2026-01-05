from pydantic import BaseModel
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: str | None = None
    status: str = "pending"


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None


class TaskResponse(TaskBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
