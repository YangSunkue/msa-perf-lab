from flask import Blueprint, jsonify
from services.external_rest import ping_service_rest

bp = Blueprint('ping', __name__, url_prefix='/rest/ping')

@bp.route('', methods=['GET'])
def ping_rest():
    """
        Go Rest 서버에 Ping 요청을 보냅니다.
    """
    result = ping_service_rest.ping_rest_service()
    return jsonify({
        'from': 'flask',
        'go_response': result
    })