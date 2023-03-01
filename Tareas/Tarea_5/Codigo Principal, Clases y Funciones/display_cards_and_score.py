# Module functions to display cards and score

#Invokes module to function to clear terminal
import clear_terminal
import class_hand

def show_some(player,dealer):
    print("\n-> Dealer's Hand")
    print("-> ", dealer.cards[1])
    print("->  <Card Hidden>")
    print("\n-> Player's Hand: ", *player.cards, sep= '\n')
    print("Player's Hand = ", player.value)

def show_all(player,dealer):
    clear_terminal.clear()
    print("\n-> Dealer's Hand:", *dealer.cards, sep="\n")
    print("Dealer's Hand =",dealer.value)
    print("\n-> Player's Hand: ", *player.cards, sep= '\n')
    print("Player's Hand = ", player.value)
