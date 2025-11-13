from flask import Blueprint, jsonify, request
from services.internal.cpu_heavy_service import cpu_heavy_service

import time

bp = Blueprint('cpu_heavy_internal', __name__, url_prefix='/internal/cpu_heavy')

@bp.route('', methods=['POST'])
def cpu_heavy_internal():
    """CPU heavy 연산을 직접 수행합니다.

    """
    data = request.get_json()
    complexity_level = data.get('complexity_level', 1)

    start_time = time.time()

    # 연산 직접 수행
    result = cpu_heavy_service(complexity_level=complexity_level)

    elapsed_time = (time.time() - start_time) * 1000 # ms

    return jsonify({
        'status': 'ok',
        'message': 'Python internal CPU heavy task completed.',
        'result_checksum': result,
        'server_time_ms': round(elapsed_time, 2)
     })