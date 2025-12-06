from Card import *
import random
class Deck:
    def __init__(self, num_decks):

        self.num_decks = num_decks
        self.cards = []
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["Clubs, Diamonds, Hearts", "Spades"]

        for card in range(num_decks):
            for suit in suits:
                for rank in ranks:
                    self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None
