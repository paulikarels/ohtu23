KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = KAPASITEETTI if kapasiteetti is None else kapasiteetti
        self.kasvatuskoko = OLETUSKASVATUS if kasvatuskoko is None else kasvatuskoko

        self.joukko = []

    def kuuluu(self, n):
        return n in self.joukko

    def lisaa(self, n):
        if self.kuuluu(n):
            return False

        if self.kapasiteetti - 1 < self.mahtavuus():
            self.joukko.append(n)
            return True
        
        self.kapasiteetti += self.kasvatuskoko
        self.joukko.append(n)
        return True


    def poista(self, n):
        if self.kuuluu(n):
            self.joukko.remove(n)


    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return len(self.joukko)


    def to_int_list(self):
        return self.joukko

    @staticmethod
    def yhdiste(a, b):
        joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(len(a_taulu)):
            joukko.lisaa(a_taulu[i])

        for i in range(len(b_taulu)):
            joukko.lisaa(b_taulu[i])
        return joukko

    @staticmethod
    def leikkaus(a, b):
        joukko = IntJoukko()
        for i in a.to_int_list():
            if b.kuuluu(i):
                joukko.lisaa(i)

        return joukko
    
    @staticmethod
    def erotus(a, b):
        joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(len(a_taulu)):
            joukko.lisaa(a_taulu[i])

        for i in range(len(b_taulu)):
            joukko.poista(b_taulu[i])

        return joukko

    def __str__(self):
        return "{%s}" % (", ".join(str(i) for i in self.to_int_list()),)
