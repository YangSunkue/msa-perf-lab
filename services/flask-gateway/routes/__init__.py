from routes.internal.user_route_internal import bp as user_internal_bp
from routes.external_rest.ping_route_rest import bp as ping_rest_bp
from routes.external_grpc.ping_route_grpc import bp as ping_grpc_bp
from routes.external_rest.mq_async_route import bp as mq_async_bp

blueprints = [
    user_internal_bp,
    ping_rest_bp,
    ping_grpc_bp,
    mq_async_bp
]