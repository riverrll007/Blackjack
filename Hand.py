"""
********************
CS 1026 Fall 2025
Assignment 4: Blackjack
Created by: River Levine LaFramenta
Student ID: rlevinel
Student Number: 251499864
File Created: December 5, 2025
********************
This file is used to represent a hand in Blackjack
"""
from Card import *
class Hand:
    #Initialize an empty hand
    def __init__(self):
        self.cards = []
    #Add a card to the hand
    def add_card(self, card):
        self.cards.append(card)
    #Calculate total value of the hand
    def total(self):
        total = 0
        aces = 0

        #Find base total, with aces starting as ones
        for card in self.cards:
            rank = card.rank
            #Face cards are worth 10
            if rank in ["J", "Q", "K"]:
                total += 10
            #Aces start a 1
            elif rank == "A":
                total += 1
                aces += 1
            else:
                total += int(rank)
        #Total without aces
        if aces == 0:
            return total
        #Lowest total with aces
        low_total = total
        #Add 10 for the higher value, with ace counting as 11
        high_total = total + 10
        #Return both possibilities
        return (low_total, high_total)
    #Return hand as string
    def __str__(self):
        #Return "Empty hand" if there are no cards in hand
        if len(self.cards) == 0:
            return "Empty hand"
        else:
            #Seperate cards with commas
            cards_str = ', '.join(str(card) for card in self.cards)
            #Get total value/s
            hand_total = self.total()
            #Format string
            if isinstance(hand_total, tuple):
                total_str = f"({hand_total[0]}, {hand_total[1]})"
            else:
                total_str = str(hand_total)
            return f"{{{cards_str}}}, Total: {total_str}"
