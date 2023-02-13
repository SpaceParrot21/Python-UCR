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

eliminar_elemento([20, 30, 40, 20, 5, 100, 5, 20], 20)
eliminar_elemento(["perro", "gato", "sombrero", "gato", "zanahoria"], "gato")
# eliminar_elemento([100, 20, 100, 40, 100, 5, 100, 5, 100], 100)
# eliminar_elemento([20, 30, 40, 10], 10)
# eliminar_elemento(["rojo", "azul", "rojo", "rosado", "rojo", "morado", "rojo", "amarillo"], "rojo")