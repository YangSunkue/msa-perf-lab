from flask import Blueprint, jsonify, request
from services.external_grpc.ping_service_grpc import ping_grpc_service

bp = Blueprint('ping_grpc', __name__, url_prefix='/grpc/ping')

@bp.route('', methods=['POST'])
def ping_grpc():
    """end_to_end/rest_vs_grpc/k6_grpc.js
        gRPC를 통해 Go 서버의 Ping 메서드를 호출합니다.

    """
    try:
        data = request.get_json(force=True)
        size = int(data.get('size', 0))

        reply = ping_grpc_service(size)

        return jsonify({
            'success': True,
            'reply': reply
        }), 200

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500