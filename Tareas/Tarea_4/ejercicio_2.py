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

# invocacion funcion y ejemplos
contador_palabras("papaya")
# contador_palabras("freecodecamp")
# contador_palabras("americano")
# contador_palabras("cofeebeans")
# contador_palabras("ortodoncista")
