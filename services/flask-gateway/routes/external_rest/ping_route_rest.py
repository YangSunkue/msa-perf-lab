from flask import Blueprint, jsonify, request
from services.external_rest import ping_service_rest

bp = Blueprint('ping', __name__, url_prefix='/rest/ping')

@bp.route('', methods=['POST'])
def ping_rest():
    """end_to_end/rest_vs_grpc/k6_rest.js
    Go Rest 서버에 Ping 요청을 보냅니다.
    
    """    
    size = int(request.args.get('size', 100_000))  # 기본값 100KB
    result = ping_service_rest.ping_rest_service(size)
    return jsonify({
        'from': 'flask',
        'go_response': result
    })