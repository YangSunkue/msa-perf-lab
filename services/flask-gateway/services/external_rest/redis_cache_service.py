from utils.redis_client import get_redis_client
from utils.prometheus_metrics import CACHE_HITS, CACHE_MISSES

from repositories import redis_cache_repository

redis_client = get_redis_client()

def count_users_by_email(email: str) -> int:
    """이메일로 사용자 수를 조회합니다.

    캐시를 활용하지 않습니다.

    Args:
        email (str): 사용자 이메일

    Returns:
        int: 해당 이메일을 가진 사용자 수
    """
    count = redis_cache_repository.count_users_by_email(email)
    return count

def count_users_by_email_with_cache(email: str, ttl: int = 60) -> int:
    """이메일로 사용자 수를 조회합니다.

    캐시를 활용합니다.

    Args:
        email (str): 사용자 이메일
        ttl (int, optional): 캐시 지속시간(초). Defaults to 60.

    Returns:
        int: 해당 이메일을 가진 사용자 수
    """
    cache_key = f'users:count:{email}'

    # 캐시 조회
    cached = redis_client.get(cache_key)
    if cached is not None:
        CACHE_HITS.labels(endpoint='with-cache').inc()
        return int(cached)
    
    # 캐시 미스 -> DB 조회
    CACHE_MISSES.labels(endpoint='with-cache').inc()
    count = redis_cache_repository.count_users_by_email(email)

    # 캐시 저장
    redis_client.setex(
        name=cache_key,
        time=ttl,
        value=count
    )

    return count