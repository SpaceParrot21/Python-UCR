# Module functions to display cards and score

#Invokes module to function to clear terminal
import clear_terminal

def show_some(player,dealer):
    print("\nDealer's Hand")
    print("-> ", dealer.cards[1])
    print("->  <Card Hidden>")
    print("\nPlayer's Hand: ", *player.cards, sep= '\n')

def show_all(player,dealer):
    clear_terminal.clear()
    print("\nDealer's Hand:", *dealer.cards, sep="\n")
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep= '\n')
    print("Player's Hand = ", player.value)