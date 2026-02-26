from ..models import Task
from .. import db

class TaskService:

    @staticmethod
    def create_task(title: str):
        if not title:
            raise ValueError("Title is required")

        task = Task(title=title)

        db.session.add(task)
        db.session.commit()

        return task

    @staticmethod
    def list_tasks():
        return Task.query.all()
    
    @staticmethod
    def get_task_by_id(task_id: int):
        task = Task.query.get(task_id)

        if not task:
            raise ValueError("Task not found")

        return task
    
    @staticmethod
    def update_task(task_id: int, data: dict):
        task = Task.query.get(task_id)

        if not task:
            raise ValueError("Task not found")

        if "title" in data:
            task.title = data["title"]

        if "completed" in data:
            task.completed = data["completed"]

        db.session.commit()

        return task

    @staticmethod
    def delete_task(task_id: int):
        task = Task.query.get(task_id)

        if not task:
            raise ValueError("Task not found")

        db.session.delete(task)
        db.session.commit()
