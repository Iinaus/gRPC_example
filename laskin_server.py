import grpc
from concurrent import futures
from laskin_pb2 import LaskuKysely, LaskuVastaus
from laskin_pb2_grpc import LaskinServicer, add_LaskinServicer_to_server

class LaskinService(LaskinServicer):
    def LaskeYhteen(self, request: LaskuKysely, context):

        tulos = request.eka + request.toka

        return LaskuVastaus(tulos=tulos)
    
    def Kertolasku(self, request: LaskuKysely, context):

        tulos = request.eka * request.toka

        return LaskuVastaus(tulos=tulos)
    
    def Miinuslasku(self, request: LaskuKysely, context):

        tulos = request.eka - request.toka

        return LaskuVastaus(tulos=tulos)
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    add_LaskinServicer_to_server(LaskinService(), server=server)

    server.add_insecure_port("[::]:50051")

    server.start()

    print("Laskin-palvelin on käynnistetty osoitteeseen [::]:50051")

    server.wait_for_termination()

if __name__ == "__main__":
    serve()