from flask import Blueprint, jsonify, request
from services.external_grpc.ping_service_grpc import ping_grpc_service

bp = Blueprint('ping_grpc', __name__, url_prefix='/grpc/ping')

@bp.route('', methods=['GET'])
def ping_grpc():
    """
        gRPC를 통해 Go 서버의 Ping 메서드를 호출합니다.
    """
    
    message = request.args.get('message', 'Hello from Flask (REST -> gRPC)')
    try:
        reply = ping_grpc_service(message)
        return jsonify({'success': True, 'reply': reply}), 200

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500