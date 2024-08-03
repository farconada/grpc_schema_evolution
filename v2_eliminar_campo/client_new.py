import grpc
import user_service_pb2
import user_service_pb2_grpc
from time import sleep

def run():
    sleep(5)
    with grpc.insecure_channel('server:50051') as channel:
        stub = user_service_pb2_grpc.UserServiceStub(channel)
        response = stub.GetUser(user_service_pb2.UserRequest(user_id=1))
        print(f"Usuario recibido: ID={response.user_id}, Nombre={response.name}")

if __name__ == '__main__':
    run()