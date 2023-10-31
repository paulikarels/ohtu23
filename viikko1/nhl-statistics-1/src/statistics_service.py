from player_reader import PlayerReader
from sort_by import SortBy

def sort_by_points(player):
    return player.points


class StatisticsService:
    def __init__(self, playerReader: PlayerReader):
        reader = playerReader

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sortBy=None):

        sorter = sort_by_points
        if (sortBy == SortBy.GOALS):
            sorter = lambda player: player.goals
        if (sortBy == SortBy.ASSISTS ):
            sorter = lambda player: player.assists
        if (sortBy == SortBy.POINTS):
            sorter = lambda player: player.goals

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sorter
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
