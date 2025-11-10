from flask import Blueprint, jsonify, request
from services.external_rest import mq_async_service

bp = Blueprint('mq_async', __name__, url_prefix='/rest/mq_async')

@bp.route('/sync', methods=['POST'])
def mq_sync():
    """동기 처리: Go 서버 호출 후 응답 대기

    K6 테스트: tests/end_to_end/mq_async/k6_sync.js
    """
    result = mq_async_service.mq_sync_service()
    return jsonify({
        'from': 'flask',
        'go_response': result,
        'type': 'sync'
    })

@bp.route('/async', methods=['POST'])
def mq_async():
    """비동기 처리: RabbitMQ에 메시지 push 후 즉시 응답

    K6 테스트: tests/end_to_end/mq_async/k6_async.js
    """
    success = mq_async_service.mq_async_service()

    if success:
        return jsonify({
            'from': 'flask',
            'status': 'accepted',
            'message': 'Task queued for processing',
            'type': 'async'
        }), 202
    
    else:
        return jsonify({
            'from': 'flask',
            'status': 'error',
            'message': 'Failed to queue task',
            'type': 'async'
        }), 500