from ..extensions import db
from ..models import Task


class TaskService:

    @staticmethod
    def list_tasks():
        return Task.query.all()

    @staticmethod
    def create_task(title):
        task = Task(title=title)
        db.session.add(task)
        db.session.commit()
        return task

    @staticmethod
    def delete_task(task_id):
        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
    @staticmethod
    def complete_task(task_id):
        task = Task.query.get(task_id)

        if not task:
            return None

        task.completed = True
        db.session.commit()

        return task
    
    @staticmethod
    def list_tasks(completed=None):

        query = Task.query

        if completed is not None:
            query = query.filter_by(completed=completed)

        return query.all()