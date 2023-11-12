from player import Player

class PlayerStats:

  def __init__(self, reader):
    self.reader = reader

  def get_players(self):
    return self.reader.read_file()
  
  def get_score(self, player):
    return player.get_score()
  
  def top_scores_by_nationality(self, nationality):
    players = []

    for player_dict in self.get_players():
        if (player_dict['nationality'] == 'FIN'):
          player = Player(player_dict)
          players.append(player)

    sorted_players = sorted(players, key=lambda p: (p.get_score()), reverse=True)

    return sorted_players