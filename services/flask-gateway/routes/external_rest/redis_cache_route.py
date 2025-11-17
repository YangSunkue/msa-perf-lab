from flask import Blueprint, jsonify
import time

from services.external_rest import redis_cache_service

bp = Blueprint('redis_cache', __name__, url_prefix='/rest/redis-cache')

@bp.route('/no-cache/<string:email>', methods=['GET'])
def count_users_by_email(email: str):
    """이메일로 사용자 수를 조회합니다.

    캐시를 활용하지 않습니다.
    """
    start_time = time.perf_counter()
    count = redis_cache_service.count_users_by_email(email)
    latency_ms = (time.perf_counter() - start_time) * 1000

    return jsonify({
        'from': 'flask',
        'status': 'ok',
        'user_count': count,
        'latency_ms': f'{latency_ms:.3f}',
        'type': 'no-cache'
    })

@bp.route('/with-cache/<string:email>', methods=['GET'])
def count_users_by_email_with_cache(email: str):
    """이메일로 사용자 수를 조회합니다.

    캐시를 활용합니다.
    """
    start_time = time.perf_counter()
    count = redis_cache_service.count_users_by_email_with_cache(email)
    latency_ms = (time.perf_counter() - start_time) * 1000

    return jsonify({
        'from': 'flask',
        'status': 'ok',
        'user_count': count,
        'latency_ms': f'{latency_ms:.3f}',
        'type': 'with-cache'
    })