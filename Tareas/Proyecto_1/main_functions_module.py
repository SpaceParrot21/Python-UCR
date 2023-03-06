'''
This module contains the functions for the following tasks:
- Display menu of users
- Show players' stats
- Show cards
- Show results 
- Handle game scenarios and save results to 'Stats.txt' file
- Save the results in the player stats file ('Stats.txt')
'''

'''All these functions require the same Global variables 
to be able to operate correctly and show the
desired results'''

# Import Clear Terminal function to keep terminal clean
# import clear_terminal as c_terminal

# Global Variables
global USUARIOS
global USUARIO_SELECIONADO

# List of predefined users
USUARIOS = ['Luis', 'John', 'Arturo', 'Melissa']
# Selected Player List
USUARIO_SELECIONADO = []

# Main function of the menu
def menu_usuarios():
    while True:
        print("\nUser Menu:")
        print("1. Select an existing user")
        print("2. Create a new user")
        print("3. Start Game")
        print("4. Exit")
        opcion = input("\nSelect an Option: ")
        clear()
        if opcion == "1":
            seleccionar_usuario()
        elif opcion == "2":
            crear_usuario()
        elif opcion == "3":
            clear()
            if len(USUARIO_SELECIONADO) == 0:
                print("\nNo user has been selected yet!!!\n")
            else:
                break
        elif opcion == "4":
            print("Good bye! The game is over.")
            quit()
        else:
            print("Invalid Option!")

# Function to display selected player statistics
def reading_statistics():

    file_name = "player_stats.txt"

    #Convert list value into 'string'
    TEXT = "".join(USUARIO_SELECIONADO)
    try:
        # Opening and Reading the file
        file_read = open(file_name, "r")
  
        # Reading file content line by line
        lines = file_read.readlines()
  
        new_list = []
        idx = 0
  
        # Looping through each line in the file
        for line in lines:
            # If line have the input string (TEXT), get the index
            # of that line and put the
            # line into newly created list
            if TEXT in line:
                new_list.insert(idx, line)
                idx += 1
  
        # Closing file after reading
        file_read.close()
  
        # If length of new list is 0 that means
        # the input string was not
        # found in the text file
        if len(new_list)==0:
            print("\n\"" +TEXT+ "\" does not have any stats in the file \"" +file_name+ "\"!")
        else:
            # Displaying the lines containing given string
            lineLen = len(new_list)
            print("\n**** These are the stats of \"" +TEXT+ "\" ****\n")
            for i in range(lineLen):
                print(end=new_list[i])
            print()
  
    # Entering except block if input file doesn't exist
    except:
        print("\nThe file doesn't exist!")

# Function to select an existing user
def seleccionar_usuario():
    print("Select an existing user")
    if len(USUARIOS) == 0:
        print("No registered users with this name.")
    else:
        print("Users:")
        for usuario in USUARIOS:
            print(usuario)
        JUGADOR = input("Select an user: ")
        clear()
        if JUGADOR in USUARIOS:
            print("\nYou have selected the user", JUGADOR,)
            # Show player stats
            USUARIO_SELECIONADO.append(JUGADOR)
            reading_statistics()
            print( "\n---> Select option '3' to start the game or option '4' to exit <---\n")
        else:
            print("Usert not found")          

# Function to create new user
def crear_usuario():
    print("Create a new user")
    JUGADOR = input("Enter the name of the new user: ")
    if JUGADOR in USUARIOS:
        print("The user already exists!")
    else:   
        USUARIOS.append(JUGADOR)
        USUARIO_SELECIONADO.append(JUGADOR)
        print("User successfully created.")

'''Module functions to handle game scenarios and
save results to 'Stats' file.'''

# Functions to handle game scenarios and save results to 'Stats.txt' file.

def player_blackjack(player,dealer):
    print("\n ---> PLAYER HAS A BLACKJACK <---")
    print(USUARIO_SELECIONADO, "won with a 'BLACKJACK'", player.value,".")
    output_file = open("player_stats.txt", "a")
    output_file.write(f"\n{USUARIO_SELECIONADO} won with a 'BLACKJACK' {player.value}.\n")
    output_file.close()
    
def player_game_over(player,dealer):
    print("\n ---> PLAYER BUSTED!!! GAME OVER!!! <---")
    print(" ---> Dealer wins! <---")

def player_wins(player,dealer):
    print("\n ---> Player wins! <---")
    print(USUARIO_SELECIONADO, "won with a total of", player.value,".")
    output_file = open("player_stats.txt", "a")
    output_file.write(f"\n{USUARIO_SELECIONADO} won with a total of {player.value}.\n")
    output_file.close()

def dealer_game_over(player,dealer):
    print("\n ---> DEALER BUSTED!!! <---")
    print(USUARIO_SELECIONADO, "won with a total of", player.value,".")
    output_file = open("player_stats.txt", "a")
    output_file.write(f"\n{USUARIO_SELECIONADO} won with a total of {player.value}.\n")
    output_file.close()

def dealer_wins(player,dealer):
    print("\n ---> Dealer wins! GAME OVER!!!<---")
    print("Dealer final score was: ", dealer.value,".")

def push(player,dealer):
    print("\n ---> Dealer and Player tie! It's a push. <---")
    print(USUARIO_SELECIONADO, "tied with",player.value,".")
    output_file = open("player_stats.txt", "a")
    output_file.write(f"\n{USUARIO_SELECIONADO} tied with {player.value}.\n")
    output_file.close()

# Module functions to display cards and score

def show_some(player,dealer):
    print("\n-> Dealer's Hand")
    print("-> ", dealer.cards[1])
    print("->  <Card Hidden>")
    print("\n-> Player's Hand: ", *player.cards, sep= '\n')
    print("Player's Hand = ", player.value)

def show_all(player,dealer):
    clear()
    print("\n-> Dealer's Hand:", *dealer.cards, sep="\n")
    print("Dealer's Hand =",dealer.value)
    print("\n-> Player's Hand: ", *player.cards, sep= '\n')
    print("Player's Hand = ", player.value)



# Function to clear terminal, to keep terminal clean

import os
# Clear the terminal
def clear():
    os.system("cls")