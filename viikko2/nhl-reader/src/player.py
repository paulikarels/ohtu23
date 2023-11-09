class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']

    
    def get_score(self):
        return self.goals+ self.assists
    
    def __str__(self):
        return (
            f"{self.name:20}"
            f" {self.team or '-'}"
            f"  {self.goals} + {self.assists} = {self.get_score()}"
        )
