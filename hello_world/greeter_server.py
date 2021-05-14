from concurrent import futures
import grpc
import main_pb2
import main_pb2_grpc


class Greeter(main_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return main_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    main_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:5000')
    print("Starting port .....")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
