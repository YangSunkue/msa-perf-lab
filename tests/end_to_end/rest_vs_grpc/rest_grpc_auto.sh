#!/bin/bash

# size를 10배씩 올려가며, rest/grpc 테스트를 순차적으로 실행합니다.
# 10rest 10grpc 100rest 100grpc ...
sizes=(10 100 1000 10000 100000 1000000)


# 테스트 코드 (데이터 저장 O)
# for size in "${sizes[@]}"; do
#     echo "=== REST test for payload size: $size ==="
#     SCENARIO_NAME="rest_ping_test_${size}" \
#     PAYLOAD_SIZE="$size" \
#     k6 run --out influxdb=http://localhost:8086/k6 k6_rest.js

#     echo "=== gRPC test for payload size: $size ==="
#     SCENARIO_NAME="grpc_ping_test_${size}" \
#     PAYLOAD_SIZE="$size" \
#     k6 run --out influxdb=http://localhost:8086/k6 k6_grpc.js
# done


#테스트 코드 (데이터 저장 X)
for size in "${sizes[@]}"; do
    echo "=== REST test for payload size: $size ==="
    SCENARIO_NAME="rest_ping_test_${size}" \
    PAYLOAD_SIZE="$size" \
    k6 run k6_rest.js

    echo "=== gRPC test for payload size: $size ==="
    SCENARIO_NAME="grpc_ping_test_${size}" \
    PAYLOAD_SIZE="$size" \
    k6 run k6_grpc.js
done