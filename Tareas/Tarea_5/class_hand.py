'''Hand class may be used to calculate the value of those cards \
    using the values dictionary defined below. It also \
        adjusts the value of Aces when appropriate'''


values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  
    
    def adjust_for_ace(self):
        # Adjust the value of Aces when appropriate
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1