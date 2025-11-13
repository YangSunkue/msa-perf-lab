#!/bin/bash

# Complexity_level을 순차적으로 올려가며, internal/external(Go gRPC) 테스트를 순차적으로 실행합니다.
# 1internal -> 1external -> 3internal -> 3external ...

# internal vs Go
# complexity_level=(1 3 5 10 25)
# complexity_level=(5 10 25)

# Go 한계측정 (600부터 병목)
complexity_level=(500 600 700 800 1000)

# 테스트 코드 (데이터 저장 O)
# for c in "${complexity_level[@]}"; do
#     echo "=== cpu heavy internal test for complexity: $c ==="
#     SCENARIO_NAME="cpu_heavy_internal_test_${c}" \
#     COMPLEXITY_LEVEL="$c" \
#     k6 run --out influxdb=http://localhost:8086/k6 k6_cpu_heavy_internal.js
#     sleep 5

#     echo "=== cpu heavy grpc test for complexity: $c ==="
#     SCENARIO_NAME="cpu_heavy_grpc_test_${c}" \
#     COMPLEXITY_LEVEL="$c" \
#     k6 run --out influxdb=http://localhost:8086/k6 k6_cpu_heavy_grpc.js
#     sleep 10
# done


#테스트 코드 (데이터 저장 X)
for c in "${complexity_level[@]}"; do
    # echo "=== cpu heavy internal test for complexity: $c ==="
    # SCENARIO_NAME="cpu_heavy_internal_test_${c}" \
    # COMPLEXITY_LEVEL="$c" \
    # k6 run k6_cpu_heavy_internal.js
    # sleep 3

    echo "=== cpu heavy grpc test for complexity: $c ==="
    SCENARIO_NAME="cpu_heavy_grpc_test_${c}" \
    COMPLEXITY_LEVEL="$c" \
    k6 run k6_cpu_heavy_grpc.js
    sleep 10
done