from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api.auth import router as auth_router
from app.api.task import router as task_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(task_router, prefix="/tasks", tags=["Tasks"])