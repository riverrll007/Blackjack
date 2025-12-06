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
                total += 11
                aces += 1
            else:
                total += int(rank)

        if aces == 0:
            return total
        # while total > 21 and aces > 0:
        #     total -= 10
        #     aces -= 1
        low_total = total - (aces * 10)
        high_total = total


        return (low_total, high_total)

    def __str__(self):
        if len(self.cards) == 0:
            return "Empty Hand"
        else:
            return f"{{{', '.join(str(card) for card in self.cards)}}}, Total: ({self.total()})"
