from random import shuffle

suits = ["Spades", "Hearts", "Diamond", "Clover"]
value = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]


class MyDeck:
    def __init__(self):
        self.cards = []
        self.create_new_deck()
        self.shuffle()

    def shuffle(self):
        shuffle(self.cards)

    def create_new_deck(self):
        for suit in suits:
            for y in value:
                self.cards.append((suit, y))

    def deal_card(self):
        return self.cards.pop(0)
