import time
from concurrent import futures
import grpc

import greeting_pb2
import greeting_pb2_grpc

class Greeter(greeting_pb2_grpc.GreetingServiceServicer):
    def greeting(self, request, context):
        print("Greeter server received : " + request.message)
        return greeting_pb2.GreetingResponse(message='Hello, %s!' % request.message)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeting_pb2_grpc.add_GreetingServiceServicer_to_server(Greeter(), server)
    server.add_insecure_port('localhost:50051')
    server.start()
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()