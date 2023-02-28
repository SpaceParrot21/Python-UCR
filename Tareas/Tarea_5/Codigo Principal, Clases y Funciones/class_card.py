class Card:
    
    def __init__(self, suit, value, rank):
        self.suit = suit
        self.rank = rank
        self.value = value
    
    def __str__(self):
        return self.rank + ' of ' + self.suit + ' ' + self.value
