from __future__ import print_function

import grpc

import greeting_pb2
import greeting_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:9091')
    stub = greeting_pb2_grpc.GreetingServiceStub(channel)
    response = stub.greeting(greeting_pb2.GreetingRequest(message='you'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()