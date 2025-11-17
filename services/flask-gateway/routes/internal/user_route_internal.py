from flask import Blueprint, jsonify
from models.user import User

bp = Blueprint('user', __name__, url_prefix='/internal/users')

@bp.route("", methods=["GET"])
def get_users_internal():
    """
        모든 사용자를 조회합니다.
    """
    users = User.query.all()
    return jsonify([user.username for user in users])