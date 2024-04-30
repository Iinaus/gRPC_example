import grpc 
from laskin_pb2_grpc import LaskinStub
from laskin_pb2 import LaskuKysely, LaskuVastaus

def run():
    channel = grpc.insecure_channel("localhost:50051")

    stub = LaskinStub(channel=channel)

    while True:
        print("Valitse laskutoimitus:")
        print("1. Yhteenlasku")
        print("2. Kertolasku")
        print("3. Vähennyslasku")
        valinta = input("Valintasi (1-3): ")

        if valinta not in ["1", "2", "3"]:
            print("Virheellinen valinta, valitse luku 1.")
            continue

        try:
            eka = int(input("Eka luku: "))
            toka = int(input("Toka luku: "))
        except ValueError:
            print("Virheellinen syöte, syötteen tulee olla kokonaislukuja")
            continue

        kysely = LaskuKysely(eka=eka, toka=toka)

        if valinta == "1":
            vastaus: LaskuVastaus = stub.LaskeYhteen(kysely)
            print(f"Summa: {vastaus.tulos}")
        elif valinta == "2":
            vastaus: LaskuVastaus = stub.Kertolasku(kysely)
            print(f"Tulo: {vastaus.tulos}")
        elif valinta == "3":
            vastaus: LaskuVastaus = stub.Miinuslasku(kysely)
            print(f"Erotus: {vastaus.tulos}")

if __name__ == "__main__":
    run() 