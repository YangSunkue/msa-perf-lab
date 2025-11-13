# gRPC

from proto import service_pb2, service_pb2_grpc
import grpc

GO_GRPC_SERVER = 'gocore:50051'

def execute_heavy_calculation(complexity_level: int) -> int:
    """CPU heavy 연산을 수행하는 Go 서버 함수를 호출합니다.

    Args:
        complexity_level (int): 연산 난이도

    Returns:
        int: 연산 결과
    """
    with grpc.insecure_channel(GO_GRPC_SERVER) as channel:
        stub = service_pb2_grpc.CpuHeavyServiceStub(channel)

        request = service_pb2.HeavyCalculationRequest(
            complexity_level=complexity_level
        )
        response = stub.ExecuteHeavyCalculation(request, timeout=10)

        return response