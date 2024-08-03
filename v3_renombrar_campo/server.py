import grpc
from concurrent import futures
import user_service_pb2
import user_service_pb2_grpc

class UserServicer(user_service_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        user_id = request.user_id
        # Simulamos obtener datos de usuario
        return user_service_pb2.UserResponse(
            user_id=user_id,
            full_name=f"Usuario {user_id}",
            email=f"usuario{user_id}@ejemplo.com"
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()