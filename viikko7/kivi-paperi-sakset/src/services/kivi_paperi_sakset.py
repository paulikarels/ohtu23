from entities.tuomari import Tuomari
from entities.tekoaly.tekoaly import Tekoaly

class KiviPaperiSakset():
    def __init__(self) :
        self._tuomari: Tuomari = Tuomari()

    def pelaa(self):
        teko = Tekoaly()
        eka_siirto = self._ensimmaisen_siirto()
        toka_siirto = teko.anna_siirto()

        while self._onko_ok_siirto(eka_siirto) and self._onko_ok_siirto(toka_siirto) :
            self._tuomari.kirjaa_siirto(eka_siirto, toka_siirto)
            print(self._tuomari)
            eka_siirto = self._ensimmaisen_siirto()
            toka_siirto = teko.anna_siirto()


        print("Kiitos!")
        print(self._tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def toisen_siirto(self, ensimmaisen_siirto):
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"