# Ejercicio 6 - Elimina repetidos

# Descripcion:
# Crea un programa que elimine los elementos repetidos
# de una lista. 

# Lista con elementos duplicados
elementos_duplicados = [1, 2, 3, 3, 2, 4, 6]

# Lista vacia sin duplicados
sin_duplicados = []

# Mensaje de error en caso de que la lista este vacia
if len(elementos_duplicados) == 0:
   print("La lista esta vacida")

# For loop para iterar entre los elementos y eliminar los duplicados
else:
    for elemento in elementos_duplicados:
        if elemento not in sin_duplicados:
            sin_duplicados.append(elemento)
    print(sin_duplicados)