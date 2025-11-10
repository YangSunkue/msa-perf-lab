#!/bin/bash

# RPS를 50씩 올려가며, sync/async 테스트를 순차적으로 실행합니다.
# 50sync 50async 100sync 100async ...
# rps=(50 100 150 200 250 300 350 400)
rps=(400)


# 테스트 코드 (데이터 저장 O)
# for r in "${rps[@]}"; do
#     echo "=== MQ sync test for rps: $r ==="
#     SCENARIO_NAME="mq_sync_test_${r}" \
#     RPS="$r" \
#     k6 run --out influxdb=http://localhost:8086/k6 k6_mq_sync.js
#     sleep 3

#     echo "=== MQ async test for rps: $r ==="
#     SCENARIO_NAME="mq_async_test_${r}" \
#     RPS="$r" \
#     k6 run --out influxdb=http://localhost:8086/k6 k6_mq_async.js
#     sleep 3
# done


#테스트 코드 (데이터 저장 X)
for r in "${rps[@]}"; do
    echo "=== MQ sync test for rps: $r ==="
    SCENARIO_NAME="mq_sync_test_${r}" \
    RPS="$r" \
    k6 run k6_mq_sync.js
    sleep 3

    echo "=== MQ async test for rps: $r ==="
    SCENARIO_NAME="mq_async_test_${r}" \
    RPS="$r" \
    k6 run k6_mq_async.js
    sleep 3
done