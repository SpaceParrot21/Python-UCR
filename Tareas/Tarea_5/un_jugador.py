import os
import random




deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4 #valor de las cartas

# record
victorias = 0
derrotas = 0

def repartir_cartas(deck):
    mano = []
    for i in range(2):
        random.shuffle(deck)
        carta = deck.pop()
        if carta == 11:carta = "J"
        if carta == 12:carta = "Q"
        if carta == 13:carta = "K"
        if carta == 14:carta = "A"
        mano.append(carta)
    return mano

def jugar_de_nuevo():
    denuevo = input("Quieres jugar de nuevo? (s/n) : ").lower()
    if denuevo == "s":
        dealer_mano = []
        jugador_mano = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        juego()
    else:
        print("Adios")
        exit()

def total(mano):
    total = 0
    for carta in mano:
        if carta == "J" or carta == "Q" or carta == "K":
            total+= 10
        elif carta == "A":
            if total >= 11: total+= 1
            else: total+= 11
        else: total += carta
    return total

def golpear(mano):
    carta = deck.pop()
    if carta == 11:carta = "J"
    if carta == 12:carta = "Q"
    if carta == 13:carta = "K"
    if carta == 14:carta = "A"
    mano.append(carta)
    return mano

def borrar():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def imprimir_resultados(dealer_mano, jugador_mano):
    borrar()

    print("\n    ¡BIENVENIDOS A BLACKJACK!\n")
    print("-"*30+"\n")
    print("    \033[1;32;40mVictorias:  \033[1;37;40m%s   \033[1;31;40mDerrotas:  \033[1;37;40m%s\n" % (victorias, derrotas))
    print("-"*30+"\n")
    print ("El dealer tiene un " + str(dealer_mano) + " por un total de " + str(total(dealer_mano)))
    print ("Usted tiene un " + str(jugador_mano) + " por un total de " + str(total(jugador_mano)))

def blackjack(dealer_mano, jugador_mano):
    global victorias
    global derrotas
    if total(jugador_mano) == 21:
        imprimir_resultados(dealer_mano, jugador_mano)
        print ("Felicidades!\n")
        victorias += 1
        jugar_de_nuevo()
    elif total(dealer_mano) == 21:
        imprimir_resultados(dealer_mano, jugador_mano)
        print ("Lo siento, pierdes.\n")
        derrotas += 1
        jugar_de_nuevo()

def record(dealer_mano, jugador_mano):
        
        global victorias
        global derrotas
        if total(jugador_mano) == 21:
            imprimir_resultados(dealer_mano, jugador_mano)
            print ("¡Felicidades! \n")
            victorias += 1
        elif total(dealer_mano) == 21:
            imprimir_resultados(dealer_mano, jugador_mano)
            print ("Lo siento, pierdes.\n")
            derrotas += 1
        elif total(jugador_mano) > 21:
            imprimir_resultados(dealer_mano, jugador_mano)
            print ("Lo siento, pierdes..\n")
            derrotas += 1
        elif total(dealer_mano) > 21:
            imprimir_resultados(dealer_mano, jugador_mano)
            print ("¡Tú ganas!\n")
            victorias += 1
        elif total(jugador_mano) < total(dealer_mano):
            imprimir_resultados(dealer_mano, jugador_mano)
            print ("Lo siento. Tu puntuación no es más alta que la del dealer. Tú pierdes.\n")
            derrotas += 1
        elif total(jugador_mano) > total(dealer_mano):
            imprimir_resultados(dealer_mano, jugador_mano)
            print ("Felicidades. Tu puntuación es más alta que la del dealer. Tú ganas\n")
            victorias += 1

def juego():
    global victorias
    global derrotas
    eleccion = 0
    borrar()
    print("\n    ¡BIENVENIDOS A BLACKJACK!\n")
    print("-"*30+"\n")
    print("    \033[1;32;40mVictorias:  \033[1;37;40m%s   \033[1;31;40mDerrotas:  \033[1;37;40m%s\n]" % (victorias, derrotas))
    print("-"*30+"\n")
    dealer_mano = repartir_cartas(deck)
    jugador_mano = repartir_cartas(deck)
    print ("El dealer está mostrando un " + str(dealer_mano[0]))
    print ("Usted tiene un " + str(jugador_mano) + " por un total de " + str(total(jugador_mano)))
    blackjack(dealer_mano, jugador_mano)
    salir=False
    while not salir:
        eleccion = input("Pedir[s] No pedir[n] salir[q] ").lower()
        if eleccion == 's':
            golpear(jugador_mano)
            print(jugador_mano)
            print("mano total: " + str(total(jugador_mano)))
            if total(jugador_mano)>21:
                print('Perdiste')
                derrotas += 1
                jugar_de_nuevo()
        elif eleccion =='n':
            while total(dealer_mano)<17:
                golpear(dealer_mano)
                print(dealer_mano)
                if total(dealer_mano)>21:
                    print(' ¡tú ganas!')
                    victorias += 1
                    jugar_de_nuevo()
            record(dealer_mano,jugador_mano)
            jugar_de_nuevo()
        elif eleccion == 'q':
            print("Adios")
            salir=True
            exit()


if __name__ == "__main__":
    juego() #llamar la funcion 

