from flask import Blueprint, jsonify, request
from .services.task_service import TaskService

main = Blueprint("main", __name__)

@main.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    try:
        task = TaskService.create_task(data.get("title"))

        return jsonify({
            "id": task.id,
            "title": task.title,
            "completed": task.completed,
            "created_at": task.created_at
        }), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@main.route("/tasks", methods=["GET"])
def list_tasks():
    tasks = TaskService.list_tasks()

    result = []
    for task in tasks:
        result.append({
            "id": task.id,
            "title": task.title,
            "completed": task.completed,
            "created_at": task.created_at
        })

    return jsonify(result), 200

