from proto import service_pb2, service_pb2_grpc
import grpc
import utils.rest_vs_grpc as util

GO_GRPC_SERVER = 'gocore:50051'

def ping_grpc_service(size: int = 0):
    """
    end_to_end/rest_vs_grpc/k6_grpc.js

    Go gRPC 서버에 Ping 요청을 보냅니다.
    """
    payload = util.generate_random_message(size)
    
    with grpc.insecure_channel(GO_GRPC_SERVER) as channel:
        stub = service_pb2_grpc.CoreServiceStub(channel)

        request = service_pb2.PingRequest(
            payload=payload
        )
        response = stub.Ping(request)

        return response.reply