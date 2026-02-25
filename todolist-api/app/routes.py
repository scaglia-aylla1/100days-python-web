from flask import Blueprint, jsonify

main = Blueprint("main", __name__)

@main.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "ok",
        "message": "API is running"
    }), 200
