import ssl
from statistics import Statistics
from player_reader import PlayerReader
from querybuilder import QueryBuilder
from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, All, Or
ssl._create_default_https_context = ssl._create_unverified_context

def main():
    url = "https://studies.cs.helsinki.fi//nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    matcher = query.playsIn("NYR").hasAtLeast(10, "goals").hasFewerThan(20, "goals").build()

    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
