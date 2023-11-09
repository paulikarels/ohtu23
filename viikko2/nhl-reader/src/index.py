import requests
from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)
    
    players = []

    for player_dict in response:
        if (player_dict['nationality'] == 'FIN'):
            player = Player(player_dict)
            players.append(player)
    
        
    sorted_players = sorted(players, key=lambda p: (p.get_score()), reverse=True)


    print("Players from FIN:\n")
    for player in sorted_players:
        print(player)

if __name__ == "__main__":
    main()