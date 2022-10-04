from random import shuffle

suits = ["Spades", "Hearts", "Diamond", "Clover"]
value = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]


class MyDeck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for y in value:
                self.cards.append((suit, y))

    def shuffle(self):
        shuffle(self.cards)
        print(self.cards)
