# Ejercicio 4 - 

# Definir variable
def convertir_a_tupla():

    # Entrada del usuario
    user_input = input("Ingrese una secuencia de numeros separados por coma: [Ejemplo:1,2,3,4,5,6]: ")

    # Enviar los valores ingresados con coma a las lista (Las comas se guardan como un valor)
    lista = (list(user_input))

    # Mensaje de error para verificar que el usuario ingrese valores separados por commas, tienen que estar separados por comas
    if "," not in user_input:
        print('Trate de nuevo, con solo numeros separados por commas, temine en una coma (e.g. "1, 5, 3,")')
        # Volver a solicitar los valores nuevamente
        user_input = input("Ingrese de nuevo secuencia de numeros separados por coma y termine con coma: [Ejemplo:1,2,3,4,5,6,]: ")
        # Enviar nuevamente los valores ingresados a la tupla en caso de que el usuario ingrese numeros diferentes en esta ocasion
        lista = (list(user_input))

    # Metodo para eliminar las comas de la lista
    for e in lista:
        # Si el valor "," esta en la lista removerlo
        if "," in lista:
            lista.remove(",")
            # Enviar los valores de la lista una tupla
            lista_a_tupla = tuple(lista)

    # Imprimir Lista y Tupla
    print(f"Lista: {lista}")
    print(f"Tupla: {lista_a_tupla}")

convertir_a_tupla()