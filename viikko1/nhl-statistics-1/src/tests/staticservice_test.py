import unittest
from statistics_service import StatisticsService
from player import Player
from sort_by import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_player_search_found(self):
        player = self.stats.search("Kurri")

        self.assertAlmostEqual(player.name, "Kurri")

    def test_player_search_not_found(self):
        found = self.stats.search("mysterio")

        self.assertAlmostEqual(found, None)

    def test_team_search(self):
        team = self.stats.team("EDM")

        self.assertAlmostEqual(len(team), 3)

        for player in team:
            self.assertAlmostEqual(player.team, "EDM")

    def test_player_score_charts(self):
        best_players = self.stats.top(1)

        self.assertAlmostEqual(len(best_players), 2)

        top_goalmaker = self.stats.top(3,SortBy.GOALS)
        self.assertEqual(top_goalmaker[0].name, "Lemieux")

        top_assists = self.stats.top(2,SortBy.ASSISTS)
        self.assertEqual(top_assists[0].name, "Gretzky")

        top_points = self.stats.top(3,SortBy.POINTS)
        self.assertEqual(top_points[0].name, "Lemieux")
