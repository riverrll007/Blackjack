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
The user will be delt two cards, and will need to make decisions to "hit" or "stand".
To win the game, the user much obtain cards with a higher value then the computer's cards
without going over 21, where they would "bust" and instantly lose.
"""
from Deck import *
from Hand import *

class Game:
    #Initialize Game with decks, hands, and variables
    def __init__(self, num_decks=1):
        self._deck = Deck(num_decks)
        self._deck.shuffle()
        self._player_hand = Hand()
        self._comp_hand = Hand()
        self._player_active = True
        self._comp_active = True
        self._results = []
    #Method to start and manage game loop
    def play(self):
        #First round
        self.play_round()
        #Additional rounds
        while True:
            again = input("Do you want to play again? (yes/no): ").strip().lower()
            if again == "yes":
                self.play_round()
            else:
                break
        #Get filename to store results once the game is over
        while True:
            filename = input("Enter filename (ending in .txt) for the game results: ").strip()
            if filename.endswith(".txt"):
                break
        #Write results to file
        self.output_game_results(filename)
    #Execute a round of Blackjack
    def play_round(self):
        #Reset hands and active status
        self._player_hand = Hand()
        self._comp_hand = Hand()
        self._player_active = True
        self._comp_active = True
        #Deal alternating cards to player and computer
        self._player_hand.add_card(self._deck.draw_card())
        self._comp_hand.add_card(self._deck.draw_card())
        self._player_hand.add_card(self._deck.draw_card())
        self._comp_hand.add_card(self._deck.draw_card())

        print(f"Player:   {self._player_hand}")
        print(f"Computer: {self._comp_hand}")
        #Continue turns when a player is active
        while self._player_active or self._comp_active:
            #Player's turn
            if self._player_active:
                turn = input(
                    "What do you want to do? Type 'hit' for another card or 'stand' if you are done. \n").strip().lower()
                #Add card if they hit
                if turn == "hit":
                    self._player_hand.add_card(self._deck.draw_card())
                    #Check if player busts
                    player_totals = self._player_hand.total()
                    if isinstance(player_totals, int):
                        player_totals = [player_totals]
                    #Busts if lower possible total is over 21
                    if min(player_totals) > 21:
                        self._player_active = False
                #End turn if they stand
                else:
                    self._player_active = False
            #Computer's turn
            if self._comp_active:
                total = self._comp_hand.total()
                #Determine low and high totals
                if isinstance(total, int):
                    low = high = total
                else:
                    low, high = total
                #Computer hit/stand logic
                if high == 21:
                    comp_move = "stand"
                elif low < 17:
                    comp_move = "hit"
                else:
                    comp_move = "stand"

                print(f"Determine what computer will do (hit/stand)\n{comp_move}")
                #Add card if they hit
                if comp_move == "hit":
                    self._comp_hand.add_card(self._deck.draw_card())
                    #Check if computer busts
                    comp_totals = self._comp_hand.total()
                    if isinstance(comp_totals, int):
                        comp_totals = [comp_totals]
                    if min(comp_totals) > 21:
                        self._comp_active = False
                #End turn if they stand
                else:
                    self._comp_active = False
            #Print hands
            print(f"Player:   {self._player_hand}")
            print(f"Computer: {self._comp_hand}")
        #Find the best valid score for player
        player_value = self._player_hand.total()
        if isinstance(player_value, int):
            player_value = [player_value]
        #Find values <= 21
        player_valid = [v for v in player_value if v <= 21]
        #Take the highest score if valid, if not take the lowest score
        player_best = max(player_valid) if player_valid else min(player_value)
        #Find the best valid score for computer
        comp_value = self._comp_hand.total()
        if isinstance(comp_value, int):
            comp_value = [comp_value]
        #Find values <= 21
        comp_valid = [v for v in comp_value if v <= 21]
        #Take the highest score if valid, if not take the lowest score
        comp_best = max(comp_valid) if comp_valid else min(comp_value)
        #Determine winner by comparing scores
        #Both busted
        if player_best > 21 and comp_best > 21:
            winner = "Neither"
        #Player busted
        elif player_best > 21:
            winner = "Computer"
        #Computer busted
        elif comp_best > 21:
            winner = "Player"
        elif player_best > comp_best:
            winner = "Player"
        elif comp_best > player_best:
            winner = "Computer"
        else:
            winner = "Draw"
        #Save results and output winner
        self._results.append((winner, player_best, comp_best))
        print(f"The round has ended. Winner: {winner}")
    #Write game results to a text file
    def output_game_results(self, filename):
        #Open new file
        with open(filename, "w") as f:
            #Track round number
            round_num = 1
            #List of round results
            output_blocks = []
            for result in self._results:
                winner, player_score, comp_score = result
                #Make scores into strings or write "bust"
                if player_score > 21:
                    player_value = "bust"
                else:
                    player_value = str(player_score)
                if comp_score > 21:
                    comp_value = "bust"
                else:
                    comp_value = str(comp_score)
                #Format output for round
                block = f"Round {round_num}\nPlayer: {player_value}\nComputer: {comp_value}\nWinner: {winner}"
                #Add to list of results
                output_blocks.append(block)
                #Update round number
                round_num += 1
            #Seperate blocks with blank lines, and ensure a trailing newline
            f.write("\n\n".join(output_blocks) + "\n")
