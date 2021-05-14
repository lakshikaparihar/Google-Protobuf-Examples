import grpc
import main_pb2
import main_pb2_grpc

user = input()
with grpc.insecure_channel('localhost:5000') as channel:
    stub = main_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(main_pb2.HelloRequest(name=user))
print(response.message)
