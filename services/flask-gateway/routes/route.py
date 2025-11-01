from flask import Blueprint, jsonify
from model import User

bp = Blueprint('user', __name__)

@bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([user.username for user in users])