from kombu import Connection, Queue
import logging
from configs import config


logger = logging.getLogger(__name__)

# 전역 Connection (Thread-safe)
_connection = None

def _get_connection():
    """전역 Connection 가져오기

    Lazy initialization
    """
    global _connection

    if _connection is None or not _connection.connected:
        conn_url = f'amqp://{config.MQ_USER}:{config.MQ_PASSWORD}@{config.MQ_HOST}:{config.MQ_PORT}//'
        _connection = Connection(conn_url)
        logger.info('RabbitMQ connected succesfully')
    
    return _connection

def publish_message(queue_name, message):
    """메시지 발행
    
    Thread-safe, Connection Pool 내장
    """
    try:
        # Connection 가져오기 (재사용)
        conn = _get_connection()

        # Producer 생성 (자동으로 Channel 관리)
        with conn.Producer() as producer:
            # 큐 정의
            queue = Queue(
                name=queue_name,
                durable=True
            )

            # 메시지 발행
            producer.publish(
                body=message,
                routing_key=queue_name,
                declare=[queue],    # 큐 자동 선언 (idempotent)
                serializer='json',
                delivery_mode=2     # 영속성
            )
        
        logger.debug(f'Message published to queue "{queue_name}"')
        return True

    except Exception as e:
        logger.error(f'Failed to publish message: {e}')

        # 예외가 발생한 Connection 정리 (다음 요청 시 새로운 Connection 만들도록 유도)
        global _connection
        if _connection:
            try:
                _connection.release()  # Connection 정상 정리 시도
            except:
                pass
            _connection = None
        
        return False