from config import conn
import unary_pb2 as output
import unary_pb2_grpc as service
import grpc

class Client():
    def __init__(self):
        self.host = 'localhost'
        self.port = 50051

        self.channel = grpc.insecure_channel(
                        '{}:{}'.format(self.host, self.port))

        self.stub = service.GreeterStub(self.channel)


    def Email_Service(self, email):
        req = output.Request(email=email)
        return self.stub.Email(req)
