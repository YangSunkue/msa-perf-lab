import grpc
from proto import service_pb2, service_pb2_grpc

GO_GRPC_SERVER = 'gocore:50051'

def ping_grpc_service(message: str = 'Hello from Flask (gRPC client)'):
    """
        Go gRPC 서버에 Ping 요청을 보냅니다.
    """
    
    with grpc.insecure_channel(GO_GRPC_SERVER) as channel:
        stub = service_pb2_grpc.CoreServiceStub(channel)

        request = service_pb2.PingRequest(message=message)
        response = stub.Ping(request)

        return response.reply