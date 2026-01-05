from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.security import get_current_user
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.services.task import create_task, list_tasks, update_task, delete_task


router = APIRouter()


@router.post("/", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    _=Depends(get_current_user)
):
    return create_task(db, task)

@router.get("/", response_model=list[TaskResponse])
def list_tasks(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, le=100),
    db: Session = Depends(get_db),
    _=Depends(get_current_user)
):
    return list_tasks(db, page, page_size)


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db),
    _=Depends(get_current_user)
):
    return update_task(db, task_id, task)


@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    _=Depends(get_current_user)
):
    delete_task(db, task_id)
    return {"message": "Task deleted"}
