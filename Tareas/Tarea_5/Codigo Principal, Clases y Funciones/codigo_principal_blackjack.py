'''Codigo Principal - BlackJack Game'''
# Import Libraries
import time

# Import Classes
import class_deck
import class_hand

# Import Functions files
import display_cards_and_score
import clear_terminal as c_terminal
import handle_game_scenarios

PLAYING = True




# function for taking hits - Posicion Original
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

# Player to take hits or stand
def hit_or_stand(deck,hand):
    global PLAYING
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ---> ")
        c_terminal.clear()

        print("\nGame in progress...... \n")
        time.sleep(2) # Sleep for 2 seconds

        # Sanity checks for player's choice
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            time.sleep(2)
            PLAYING = False

        else:
            print("Sorry, please try again.")
            continue
        break

#Start Game opening message and user selection
while True:
    # Selecione el usuario con el que desea jugar


    
    # Print an opening statement
    print("Welcome to the Blackjack game. The game has started...")
    time.sleep(1) # Sleep for 1 seconds
    # Print Shuffling Deck to mimick dealer shuffling the Deck
    print("Shuffling the Deck....")
    time.sleep(1.5) # Sleep for 1.5 seconds
    print("Shuffling the Deck....")
    time.sleep(1) # Sleep for 1 seconds
    print("Shuffling the Deck....")
    time.sleep(0.5) # Sleep for 0.5 seconds

    # Create & shuffle the deck, deal two cards to each player
    deck = class_deck.Deck() # Calls Deck function
    deck.shuffle()

    player_hand = class_hand.Hand()  # Calls Hand function
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand = class_hand.Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Show cards (but keep one dealer card hidden)
    display_cards_and_score.show_some(player_hand, dealer_hand) # CallS function to display some cards fucntion

    while PLAYING:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        display_cards_and_score.show_some(player_hand,dealer_hand)

        # If player's hand exceeds 21, run player_game_over() and break out of loop
        if player_hand.value >21:
            handle_game_scenarios.player_game_over(player_hand, dealer_hand) # Calls function player_game_over() on game scenarios module
            display_cards_and_score.show_all(player_hand,dealer_hand) # CallS function to display all cards function
            break
        # If dealer's hand is equal 21, run dealer_wins() and break out of loop
        elif dealer_hand.value == 21:
            handle_game_scenarios.dealer_wins(player_hand,dealer_hand)
            display_cards_and_score.show_all(player_hand,dealer_hand) # CallS function to display all cards function
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 19
    if player_hand.value <= 21:

        while dealer_hand.value <19:
            # hit(deck, dealer_hand)
            hit(deck, dealer_hand)
            display_cards_and_score.show_all(player_hand,dealer_hand) # CallS function to display all cards function

        # Run different winning scenarios
        if player_hand.value == 21:
            handle_game_scenarios.player_blackjack(player_hand,dealer_hand)
        elif dealer_hand.value > 21:
            handle_game_scenarios.dealer_game_over(player_hand,dealer_hand)
        elif dealer_hand.value > player_hand.value:
            handle_game_scenarios.dealer_wins(player_hand,dealer_hand)
        elif dealer_hand.value < player_hand.value:
            handle_game_scenarios.player_wins(player_hand,dealer_hand)
        else:
            handle_game_scenarios.push(player_hand,dealer_hand)

    # Ask to play again
    new_game = input("Would you like to play again? Enter 'y' or 'n' ---> ")
    # c_terminal.clear()
    if new_game[0].lower() == 'y':
        PLAYING = True
        c_terminal.clear()
        continue
    elif new_game[0].lower() == 'n':
            print('Thanks for playing! The game is over.\n')      
    else:
        print("Sorry, please try again.")
        continue
    break