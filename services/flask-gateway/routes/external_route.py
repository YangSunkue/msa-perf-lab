from flask import Blueprint, jsonify
import services.go_service as go

bp = Blueprint("external", __name__, url_prefix="/external")

@bp.route("/ping", methods=["GET"])
def ping_external():
    result = go.ping()
    return jsonify({
        "from": "flask",
        "go_response": result
    })