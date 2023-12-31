from services.kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from services.kps_tekoaly import KPSTekoaly
from services.kps_parempi_tekoaly import KPSParempiTekoaly

class Pelaa:
    def __init__(self):
        pass

    @staticmethod
    def yksinpeli():
        return KPSTekoaly().pelaa()

    @staticmethod
    def kaksinpeli():
        return KPSPelaajaVsPelaaja().pelaa()

    @staticmethod
    def haastava_yksinpeli():
        return KPSParempiTekoaly().pelaa()