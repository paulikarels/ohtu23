class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = {'name': player1_name, 'score' : 0}
        self.player2 = {'name': player2_name, 'score' : 0}
        self.scores = ["Love", "Fifteen", "Thirty", "Forty"]
        
    def won_point(self, player_name):
        if player_name == self.player1['name']:
            self.player1['score'] += 1
        else:
            self.player2['score'] += 1

    def get_score(self):

        if self.player1['score'] == self.player2['score']:
            return self.format_score(self.player1['score'])

        elif max(self.player1['score'] , self.player2['score']) >= 4 :
                score_diff = self.player1['score'] - self.player2['score']
                ahead_player = self.player1['name'] if score_diff > 0 else self.player2['name']
                if abs(score_diff) == 1:
                    return f"Advantage {ahead_player}"
                return f"Win for {ahead_player}"

        else:
            return f"{self.scores[self.player1['score']]}-{self.scores[self.player2['score']]}"
        

    def format_score(self, points):
        
        if points >= 3:
            return "Deuce"

        return f"{self.scores[points]}-All"

    def _get_by_diff(self):
        score_diff = self.player1['score'] - self.player2['score']
        ahead_player = self.player1['name'] if score_diff > 0 else self.player2['name']
        if abs(score_diff) == 1:
            return f"Advantage {ahead_player}"
        return f"Win for {ahead_player}"
