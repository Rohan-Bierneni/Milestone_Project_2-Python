

class Player:

    def __init__(self):
        self.name = ""
        self.bet = 0
        self.count = 0
        self.wins = 0
        self.losses = 0
        self.player_cards = []


    def win_game(self):
        self.wins += 1

    def lose_game(self):
        self.losses += 1
