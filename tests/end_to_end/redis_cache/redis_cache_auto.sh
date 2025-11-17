#!/bin/bash

# RPS를 순차적으로 올려가며, no-cache/with-cache 테스트를 순차적으로 실행합니다.
# 30no-cache -> 30with-cache -> 500no-cache -> 500with-cache ...

# 매번 캐시 지우면서 진행, 300에서 막히는거 보여주고
rps=(30 50 75 100 150 300)

# 캐시 안지우고 300 하는거 보여줘서 캐시 효과 입증
# rps=(150 300 500 1000)

# 테스트 코드 (데이터 저장 O)
for r in "${rps[@]}"; do
    echo "=== no-cache test for rps: $r ==="
    SCENARIO_NAME="no_cache_${r}RPS" \
    RATE="$r" \
    k6 run --out influxdb=http://localhost:8086/k6 k6_no_cache.js
    sleep 5

    echo "=== with-cache test for rps: $r ==="
    SCENARIO_NAME="with_cache_${r}RPS" \
    RATE="$r" \
    k6 run --out influxdb=http://localhost:8086/k6 k6_with_cache.js
    docker exec msa-perf-redis redis-cli FLUSHALL
    sleep 5
done


#테스트 코드 (데이터 저장 X)
# for r in "${rps[@]}"; do
    # echo "=== no-cache test for rps: $r ==="
    # SCENARIO_NAME="no_cache_${r}RPS" \
    # RATE="$r" \
    # k6 run k6_no_cache.js
    # sleep 5

#     echo "=== with-cache test for rps: $r ==="
#     SCENARIO_NAME="with_cache_${r}RPS" \
#     RATE="$r" \
#     k6 run k6_with_cache.js
#     docker exec msa-perf-redis redis-cli FLUSHALL
#     sleep 5
# done