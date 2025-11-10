from utils.rabbitmq_client import publish_message
import requests

GO_SERVER_BASE_URL = 'http://gocore:8080'
QUEUE_NAME = 'mq_async_tasks'

def mq_sync_service():
    """동기 처리: Go 서버에 요청 보내고 응답 대기

    Go 서버에서 sleep(1초) 후 응답하므로
    Flask는 최소 1초 이상 대기하게 된다.
    """
    try:
        res = requests.post(
            f'{GO_SERVER_BASE_URL}/mq_async/delay',
            json={'action': 'delay'},
            timeout=10
        )
        res.raise_for_status()
        return res.json()
    
    except requests.RequestException as e:
        return {'error': str(e)}

def mq_async_service():
    """비동기 처리: RabbitMQ에 메시지 발행

    메시지 발행 후 즉시 성공여부를 리턴한다.
    """
    try:
        message = {'action': 'delay'}
        success = publish_message(QUEUE_NAME, message)
        return success

    except Exception as e:
        print(f'Failed to publish to RabbitMQ: {e}')
        return False