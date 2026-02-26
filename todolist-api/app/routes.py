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

@main.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    try:
        task = TaskService.get_task_by_id(task_id)

        return jsonify({
            "id": task.id,
            "title": task.title,
            "completed": task.completed,
            "created_at": task.created_at
        }), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@main.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    try:
        data = request.get_json()

        task = TaskService.update_task(task_id, data)

        return jsonify({
            "id": task.id,
            "title": task.title,
            "completed": task.completed,
            "created_at": task.created_at
        }), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 404
