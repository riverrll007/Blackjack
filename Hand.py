from Card import *
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def total(self):
        total = 0
        aces = 0

        for card in self.cards:
            rank = card.rank

            if rank in ["J", "Q", "K"]:
                total += 10
            elif rank == "A":
                total += 1
                aces += 1
            else:
                total += int(rank)

        if aces == 0:
            return total

        low_total = total
        high_total = + 10

        return (low_total, high_total)

    def __str__(self):
        if len(self.cards) == 0:
            return "Empty hand"
        else:
            cards_str = ', '.join(str(card) for card in self.cards)
            hand_total = self.total()
            if isinstance(hand_total, tuple):
                total_str = f"({hand_total[0]}, {hand_total[1]})"
            else:
                total_str = str(hand_total)
            return f"{{{cards_str}}}, Total: {total_str}"

