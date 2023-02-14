'''

Tarea 4 - Este documento cuenta con todas la funciones para los 4 ejercicios

'''

# Ejercicio 1 - Contar cantidad de Letras, numero y caracteres especiales en un string.

# Definicion del nombre de la funcion
def conteo_letras_numeros_caracteres (string_prueba):
    
    #Definir variables
    numeros = 0
    letras = 0
    caracteres_especiales = 0

    # Verificacion de tipo de datos en un string + conteo
    for i in string_prueba:
        if i.isdigit():
            numeros = numeros + 1
        elif i.isalpha():
            letras += 1
        else:
            caracteres_especiales += 1
    
    # Imprimir totales
    print(f"Cantidad de letras: {letras}")
    print(f"Cantidad de numeros: {numeros}")
    print(f"Cantidad de caracteres especiales: {caracteres_especiales}")
    return numeros, letras, caracteres_especiales

# Invocacion de la funcion y casos de prueba
# conteo_letras_numeros_caracteres("P@#yn26at^&i5ve")
# conteo_letras_numeros_caracteres("Querty-21")
# conteo_letras_numeros_caracteres("Pyl@nc'3r-23")
# conteo_letras_numeros_caracteres("Prueba4_56")
# conteo_letras_numeros_caracteres("asdf4534")


# Ejercicio 2 - Conteo occuerencias de palabras en un string

def contador_palabras(palabra):

    # Diccionario vacido y dividir la palabra en caracteres individuales con el metodo list()
    diccionario = {}
    letras = list(palabra)

    # Sentencia condicional for para hacer conteo iterativo de las letras en la palabra
    for letra in letras:
        if letra not in diccionario:
            diccionario[letra] = 1
        else:
            diccionario[letra] += 1

    # Imprimir el diccionario
    print(diccionario)

# Invocacion de la funcion y casos de prueba
# contador_palabras("papaya")
# contador_palabras("freecodecamp")
# contador_palabras("americano")
# contador_palabras("cofeebeans")
# contador_palabras("ortodoncista")


# Ejercicio 3- Eliminar todas las apariciones de un elemento en una lista.

def eliminar_elemento(lista_de_parametro, valor):

    # For loop en los elementos de la lista
    for e in lista_de_parametro:

        # Si el valor esta en la lista removerlo
        if valor in lista_de_parametro:
            lista_de_parametro.remove(valor)
        # Si no esta continuar con el siguiente elemento
        else:
            continue

    print(lista_de_parametro)

# Invocacion de la funcion y casos de prueba
# eliminar_elemento([20, 30, 40, 20, 5, 100, 5, 20], 20)
# eliminar_elemento(["perro", "gato", "sombrero", "gato", "zanahoria"], "gato")
# eliminar_elemento([100, 20, 100, 40, 100, 5, 100, 5, 100], 100)
# eliminar_elemento([20, 30, 40, 10], 10)
# eliminar_elemento(["rojo", "azul", "rojo", "rosado", "rojo", "morado", "rojo", "amarillo"], "rojo")


# Ejercicio 4 - Ingresar numeros separados por coma y imprimirlos en una lista y una tupla

# Definir variable
def convertir_a_tupla():

    # Entrada del usuario - Probar con varios casos
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

# Invocacion de la funcion
# convertir_a_tupla()
