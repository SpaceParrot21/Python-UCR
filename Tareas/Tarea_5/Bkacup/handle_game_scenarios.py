# Functions to handle game scenarios

def player_blackjack(player,dealer):
    print("\n ---> PLAYER HAS A BLACKJACK <---")
    
def player_game_over(player,dealer):
    print("\n ---> PLAYER BUSTED!!! GAME OVER!!! <---")
    print(" ---> Dealer wins! <---")

def player_wins(player,dealer):
    print("\n ---> Player wins! <---")
    print("Player final score was: ", player.value)
    # Aqui se podria guardar el score del usuario en un file

def dealer_game_over(player,dealer):
    print("\n ---> DEALER BUSTED!!! GAME OVER!!! <---")
    print(" ---> Player wins! <---")

def dealer_wins(player,dealer):
    print("\n ---> Dealer wins! <---")
    print("Dealer final score was: ", dealer.value)

def push(player,dealer):
    print("\n ---> Dealer and Player tie! It's a push. <---")
