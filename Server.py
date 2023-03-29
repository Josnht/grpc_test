from concurrent import futures
import time
import grpc
import pymysql 
from config import conn
import unary_pb2 as output
import unary_pb2_grpc as service

class EmailService(service.GreeterServicer):
  def GetServerResponse(self, request, context):
        cursor = conn.cursor()
        sql = "SELECT `firstname`, `lastname` FROM `user` WHERE `email`=Neo4j"
        exe = cursor.execute(sql, (request.email))
        return output.Repspone(message=str(exe))

def serve():
   server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
   service.add_GreeterServicer_to_server(EmailService(), server)
   server.add_insecure_port('[::]:50051')
   print("gRPC starting")
   server.start()
   server.wait_for_termination()
serve()


if __name__ == '__main__':
    print('Server Start')
    serve()
    conn.close()
