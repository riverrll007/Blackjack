from Card import *

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def total(self):
        total_low = 0
        aces = 0

        for card in self.cards:
            rank = card.get_rank()
            if rank == "A":
                aces += 1
                total_low += 1
            elif rank in ["J", "Q", "K"]:
                total_low += 10
            else:
                total_low += int(rank)

        if aces == 0:
            return total_low

        total_high = total_low + 10
        return (total_low, total_high)

    def __str__(self):
        if len(self.cards) == 0:
            return "Empty hand"

        inside = ", ".join([str(card) for card in self.cards])
        total_val = self.total()
        return "{" + inside + "}, Total: " + str(total_val)

