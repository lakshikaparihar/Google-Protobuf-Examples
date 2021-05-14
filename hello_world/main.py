import main_pb2
import sys

person = main_pb2.HelloRequest()
person.name= input()
print(main_pb2.HelloReply(message='Hello, %s!' %person.name))
details = main_pb2.HelloReply()
print(details.message)
