import Deck
import Player
import Dealer


class Blackjack:
    player = Player.Player()
    deck = Deck.MyDeck()
    dealer = Dealer.Dealer()

    def __init__(self):
        self.start_game()

    def player_count_cards(self, player=player):
        for card in player.player_cards:
            player.count += self.card_value(card)
        return player.count

    def dealer_count_cards(self, dealer=dealer):
        for card in dealer.dealer_cards:
            dealer.count += self.card_value(card)
        return dealer.count

    def card_value(self, card):
        if card[1] == "Ten" or card[1] == "Jack" or card[1] == "Queen" or card[1] == "King":
            return 10
        normal_cards = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5,
            "Six": 6,
            "Seven": 7,
            "Eight": 8,
            "Nine": 9,
            "Ace": 11
        }
        return normal_cards[card[1]]

    def start_game(self, player=player, dealer=dealer, deck=deck):
        player.player_cards.append(deck.deal_card())
        player.player_cards.append(deck.deal_card())

        dealer.dealer_cards.append(deck.deal_card())
        dealer.dealer_cards.append(deck.deal_card())

        player.name = input("Enter the player's name: ")
        player.bet = int(input("How much would you like to bet: "))

        flag = True
        while flag:
            print(f'Current count of player is: {self.player_count_cards()}')
            choice = int(input("Would you like to stand or hit(0 or 1): "))
            if choice == 1:
                card = deck.deal_card()
                player.player_cards.append(card)
                if self.player_count_cards(player) > 21:
                    player.losses += 1
                    flag = False
                    player.bet = 0
                elif self.player_count_cards(player) == 21:
                    player.wins += 1
                    flag = False
                    player.bet = 0
                else:
                    pass
            else:
                # code for dealer to pull
                flag = False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = Blackjack()
