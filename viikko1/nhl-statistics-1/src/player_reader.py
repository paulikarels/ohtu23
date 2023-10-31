
from urllib import request
from player import Player

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

class PlayerReader:
    def __init__(self, url):
        self._url = url
    def get_players(self):
        players_file = request.urlopen(self._url)
        #players_file = request.urlopen(self._url, cafile=certifi.where())
        players = []

        for line in players_file:
            decoded_line = line.decode("utf-8")
            parts = decoded_line.split(";")

            if len(parts) > 3:
                player = Player(
                    parts[0].strip(),
                    parts[1].strip(),
                    int(parts[3].strip()),
                    int(parts[4].strip())
                )

                players.append(player)

        return players
