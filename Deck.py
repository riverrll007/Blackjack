"""
********************
CS 1026 Fall 2025
Assignment 4: Blackjack
Created by: River Levine LaFramenta
Student ID: rlevinel
Student Number: 251499864
File Created: December 5, 2025
********************
This class represents a deck of cards used in a game of Blackjack.
It can also include multiple standard decks combined.
"""
from Card import *
import random
class Deck:
    #Initialize the Deck object with a number of standard 52 card decks
    def __init__(self, num_decks):
        self.num_decks = num_decks
        self.cards = []
        #Order ranks: A, 2-10, J, Q, K
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        #Order suits alphabetically: C, D, H, S
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        #Loop to make # of decks
        for deck in range(num_decks):
            #Cycle through suits then ranks and add them to the deck
            for suit in suits:
                for rank in ranks:
                    self.cards.append(Card(rank, suit))

    def shuffle(self):
        #Shuffle the deck randomly
        random.shuffle(self.cards)

    def draw_card(self):
        #Remove and return the top card of the deck
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return None
