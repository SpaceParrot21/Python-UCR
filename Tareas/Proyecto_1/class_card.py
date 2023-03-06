'''Class to create a proper deck of cards containing 52 Card objects (deck)
with the help of class_deck.py class to retrun
 a string in the form “Two of Hearts + unicode value”'''

class Card:
    
    def __init__(self, suit, value, rank):
        #Declare ensemble of suits, ranks and values
        self.suit = suit # Suit of the Card
        self.rank = rank # Attribute card object
        self.value = value # Representing Value of the Card in a diccionary in (class_deck.py) like Spades" and unicode "\u2664".
    
    def __str__(self):
        return self.rank + ' of ' + self.suit + ' ' + self.value
