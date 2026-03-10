from flask.views import MethodView
from flask_smorest import Blueprint

from .services.task_service import TaskService
from .schemas.task_schema import TaskSchema, TaskCreateSchema, TaskCompleteSchema

blp = Blueprint(
    "tasks",
    __name__,
    url_prefix="/tasks",
    description="Operations on tasks"
)


@blp.route("/")
class TaskList(MethodView):

    @blp.response(200, TaskSchema(many=True))
    def get(self):
        """List all tasks"""
        return TaskService.list_tasks()

    @blp.arguments(TaskCreateSchema)
    @blp.response(201, TaskSchema)
    def post(self, data):
        """Create a new task"""
        return TaskService.create_task(data["title"])


@blp.route("/<int:task_id>")
class TaskDetail(MethodView):

    def delete(self, task_id):
        """Delete a task"""
        TaskService.delete_task(task_id)
        return {"message": "Task deleted"}, 204

    @blp.arguments(TaskCompleteSchema)
    @blp.response(200, TaskSchema)
    def patch(self, data, task_id):
        """Mark a task as completed"""

        if data["completed"] is not True:
            return {"message": "Only completed=True is allowed"}, 400

        task = TaskService.complete_task(task_id)

        if not task:
            return {"message": "Task not found"}, 404

        return task
