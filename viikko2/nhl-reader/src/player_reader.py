import requests

class PlayerReader:

    def __init__(self, url):
        self.url = url

    def read_file(self):
        return requests.get(self.url).json()