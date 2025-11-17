import redis

from configs import config

redis_client = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=config.REDIS_DB,
    decode_responses=True  # 자동으로 bytes -> str 변환
)

def get_redis_client():
    """Redis 클라이언트를 반환합니다."""
    return redis_client