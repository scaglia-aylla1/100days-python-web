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
