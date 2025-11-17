from prometheus_client import Counter

# Redis 캐시 히트 카운터
CACHE_HITS = Counter(
    'redis_cache_hits_total',
    'Total number of cache hits on Redis (per endpoint)',
    ['endpoint']
)

# Redis 캐시 미스 카운터
CACHE_MISSES = Counter(
    'redis_cache_misses_total',
    'Total number of cache misses on Redis (per endpoint)',
    ['endpoint']
)