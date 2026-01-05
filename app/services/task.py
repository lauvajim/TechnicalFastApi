from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


def create_task(db: Session, task: TaskCreate) -> Task:
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def list_tasks(
    db: Session,
    page: int,
    page_size: int
) -> list[Task]:
    offset = (page - 1) * page_size

    return (
        db.query(Task)
        .order_by(Task.created_at.desc())
        .offset(offset)
        .limit(page_size)
        .all()
    )


def get_task_by_id(db: Session, task_id: int) -> Task:
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


def update_task(
    db: Session,
    task_id: int,
    data: TaskUpdate
) -> Task:
    task = get_task_by_id(db, task_id)

    for key, value in data.dict(exclude_unset=True).items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task_id: int) -> None:
    task = get_task_by_id(db, task_id)
    db.delete(task)
    db.commit()
