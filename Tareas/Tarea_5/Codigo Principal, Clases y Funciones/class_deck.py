import class_card
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
# suits = ('\u2764', '\u2666', '\u2660', '\u2618')
suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list#
        for suit in suits:
            for rank in ranks:
                # self.deck.append(class_card.Card(suit, rank))
                self.deck.append(class_card.Card(suit, suits_values[suit], rank))
                # suits_values[suit]
    
    def __str__(self):
        deck_comp = '' #strating competition deck empty#
        for card in self.deck:
            deck_comp += '\n' + card.__str__() #add each card object;s strin#
        return 'The deck has' + deck_comp
            
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
