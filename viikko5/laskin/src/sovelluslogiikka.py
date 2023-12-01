class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self.edellinen = None

    def miinus(self, operandi):
        self.edellinen = self._arvo
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self.edellinen = self._arvo
        self._arvo = self._arvo + operandi
        
    def nollaa(self):
        self._arvo = 0

    def kumoa(self):
        if self.edellinen:
            self._arvo = self.edellinen
        self.edellinen = None
    
class Summa:
    def __init__(self, sovellus, arvo):
        self._sovellus = sovellus
        self._arvo = arvo
    def suorita(self):
        self._sovellus.plus(int(self._arvo()))

class Erotus:
    def __init__(self, sovellus, arvo):
        self._sovellus = sovellus
        self._arvo = arvo
    def suorita(self):
        self._sovellus.miinus(int(self._arvo()))

class Nollaus:
    def __init__(self, sovellus):
        self._sovellus = sovellus
    def suorita(self):
        self._sovellus.nollaa()

class Kumoa:
    def __init__(self, sovellus, arvo):
        self._sovellus = sovellus
        self._arvo = arvo
    def suorita(self):
        self._sovellus.kumoa()