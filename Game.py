"""
********************
CS 1026 Fall 2025
Assignment 4: Blackjack
Created by: River Levine LaFramenta
Student ID: rlevinel
Student Number: 251499864
File Created: December 5, 2025
********************
This file is used to simulate a game of Blackjack.
The game is in the format of player vs computer.
The user will be delt two cards, and will need to make decisions to "hit" or "hold".
To win the game, the user much obtain cards with a higher value then the computer's cards
without going over 21, where they would "bust" and instantly lose.
"""
from Deck import *
from Hand import *
class Game:
    def __init__(self, num_decks = 1):
        self._deck = Deck(num_decks)
        self._deck.shuffle()

        self._player_hand = Hand()
        self._comp_hand = Hand()
        self._player_active = True
        self._comp_active = True
        self._results = []

    def play(self):

        self.play_round()

        while True:
            again = input("Would you like to play another round? (yes/no): ").strip().lower()

            if again == "yes":
                self.play_round()
            else:
                break
        while True:
            filename = input("Enter a filename ending in .txt: ").strip()
            if filename.endswith(".txt"):
                break

        self.output_game_results(filename)

    def play_round(self):

        self._player_hand = Hand()
        self._comp_hand = Hand()
        self._player_active = True
        self._comp_active = True

        self._player_hand.add_card(self._deck.draw_card())
        self._comp_hand.add_card(self._deck.draw_card())
        self._player_hand.add_card(self._deck.draw_card())
        self._comp_hand.add_card(self._deck.draw_card())

        print(f"Player:   {self._player_hand}")
        print(f"Computer: {self._comp_hand}")

        while self._player_active or self._comp_active:
            if self._player_active:
                turn = input(
                    "What do you want to do? Type 'hit' for another card or 'stand' if you are done. \n").strip().lower()
                if turn == "hit":
                    self._player_hand.add_card(self._deck.draw_card())
                else:
                    self._player_active = False

                player_totals = self._player_hand.total()
                if isinstance(player_totals, int):
                    player_totals = [player_totals]
                if min(player_totals) > 21:
                    self._player_active = False

            if self._comp_active:
                total = self._comp_hand.total()
                if isinstance(total, int):
                    low = high = total
                else:
                    low, high = total

                if high == 21:
                    comp_move = "stand"
                elif low < 17:
                    comp_move = "hit"
                else:
                    comp_move = "stand"

                print(f"Determine what computer will do (hit/stand)\n{comp_move}")

                if comp_move == "hit":
                    self._comp_hand.add_card(self._deck.draw_card())
                    comp_totals = self._comp_hand.total()
                    if isinstance(comp_totals, int):
                        comp_totals = [comp_totals]
                    if min(comp_totals) > 21:
                        self._comp_active = False
                else:
                    self._comp_active = False

            print(f"Player:   {self._player_hand}")
            print(f"Computer: {self._comp_hand}")

        player_value = self._player_hand.total()
        if isinstance(player_value, int):
            player_value = [player_value]
        player_valid = [v for v in player_value if v <= 21]
        player_best = max(player_valid) if player_valid else min(player_value)

        comp_value = self._comp_hand.total()
        if isinstance(comp_value, int):
            comp_value = [comp_value]
        comp_valid = [v for v in comp_value if v <= 21]
        comp_best = max(comp_valid) if comp_valid else min(comp_value)

        if player_best > 21 and comp_best > 21:
            winner = "Neither"
        elif player_best > 21:
            winner = "Computer"
        elif comp_best > 21:
            winner = "Player"
        elif player_best > comp_best:
            winner = "Player"
        elif comp_best > player_best:
            winner = "Computer"
        else:
            winner = "Draw"

        self._results.append((winner, player_best, comp_best))
        print(f"The round has ended. Winner: {winner}")

    def output_game_results(self, filename):
        with open(filename, "w") as f:
            round_num = 1

            for result in self._results:
                winner, player_score, comp_score = result

                if player_score > 21:
                    player_value = "bust"
                else:
                    player_value = str(player_score)
                if comp_score > 21:
                    comp_value = "bust"
                else:
                    comp_value = str(comp_score)

                f.write(f"Round {round_num}\n")
                f.write(f"Player: {player_value}\n")
                f.write(f"Computer: {comp_value}\n")
                f.write(f"Winner: {winner}\n")


                f.write("\n")
                round_num += 1
        with open(filename, "a") as f:
            f.write("")
