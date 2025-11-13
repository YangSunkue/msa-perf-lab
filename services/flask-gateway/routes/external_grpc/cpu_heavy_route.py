# gRPC

from flask import Blueprint, jsonify, request
from services.external_grpc.cpu_heavy_service import execute_heavy_calculation

import time, grpc

bp = Blueprint('cpu_heavy_grpc', __name__, url_prefix='/grpc/cpu_heavy')

@bp.route('', methods=['POST'])
def cpu_heavy_grpc():
    """CPU heavy 연산을 수행하는 Go 서버 함수를 호출합니다.

    """
    data = request.get_json()
    complexity_level = data.get('complexity_level', 1)

    start_time = time.time()

    try:

        # Go 서버로 CPU 연산 위임
        response = execute_heavy_calculation(complexity_level=complexity_level)

        elapsed_time = (time.time() - start_time) * 1000 # ms

        return jsonify({
            'status': 'ok',
            'message': 'Go gRPC CPU heavy task completed.',
            'success': response.success,
            'result_checksum': response.result_checksum,
            'server_time_ms': round(elapsed_time, 2)
        })
    
    except grpc.RpcError as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500