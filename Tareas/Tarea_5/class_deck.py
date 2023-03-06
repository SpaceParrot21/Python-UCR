'''Using the values suits, suit values, ranks and
the Card Class, we generate a deck of cards, 
shuffle our deck, and to deal out cards during gameplay'''

# Import Library
import random

# Import class
import class_card


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
class Deck:
    
    # Methods to shuffle our deck, and to deal out cards during gameplay.
    def __init__(self):
        self.deck = []  # Start with an empty list
        # instantiating all 52 unique card objects and add them to the list.
        for suit in suits: # Iterating over sequences of suits and ranks to build out each card.
            for rank in ranks:
                self.deck.append(class_card.Card(suit, suits_values[suit], rank))
    
    def __str__(self):
        deck_comp = '' # Starting with a competition deck empty
        for card in self.deck:
            deck_comp += '\n' + card.__str__() # Add each card object's string
        return 'The deck has' + deck_comp

    # Methods to shuffle our deck,        
    def shuffle(self):
        random.shuffle(self.deck)
    
    # Method to deal out cards during gameplay
    def deal(self):
        single_card = self.deck.pop()
        return single_card
