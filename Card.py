"""
********************
CS 1026 Fall 2025
Assignment 4: Blackjack
Created by: River Levine LaFramenta
Student ID: rlevinel
Student Number: 251499864
File Created: December 5, 2025
********************
This class represents a card from a standard deck of cards.
"""

class Card:

    #Initializes the Card object with a specific rank and suit
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    #Returns the rank of the card
    def get_rank(self):
        return self.rank
    #Returns the suit of the card
    def get_suit(self):
        return self.suit
    #Returns the card as a string
    def __str__(self):
        return f'{self.rank}{self.suit[0].upper()}'
    #Determines if the card is equal to another card
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.rank == other.rank and self.suit == other.suit
        return False
