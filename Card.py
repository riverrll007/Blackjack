class Card:
    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    def __str__(self):
        return f'{self.rank}{self.suit[0].upper()}'

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.rank == other.rank and self.suit == other.suit
        return False
