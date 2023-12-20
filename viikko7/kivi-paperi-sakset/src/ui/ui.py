from services.peliolio import Pelaa

class UI:
    def __init__(self):
        self.__ohje: str = "\n".join(
            [
                "Valitse pelataanko",
                "(a) Ihmistä vastaan",
                "(b) Tekoälyä vastaan",
                "(c) Parannettua tekoälyä vastaan",
                "Muilla valinnoilla lopetetaan",
            ]
        )

    def kaynnista(self):
        while True:
            self.__tulosta_ohje()

            vaikeus = input()

            try:
                print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s") 
                self.__kaynnista_peli(vaikeus)
            except KeyError:
                return

    def __tulosta_ohje(self):
        print(self.__ohje)

    def __kaynnista_peli(self, vaikeus):
      while True:
        if vaikeus.endswith("a"):
            Pelaa.kaksinpeli()
        elif vaikeus.endswith("b"):
            Pelaa.yksinpeli()
        elif vaikeus.endswith("c"):
            Pelaa.haastava_yksinpeli()
        else:
            break
