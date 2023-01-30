# Ejercicio 3 - Strings intercaladas

# Descripcion:  
# Escriba un programa que reciba dos strings del mismo
# largo por parte del usuario e imprima una nueva string con los caracteres de
# ambos inputs intercalados.

# Variables para almacenar las palabras ingresadas por el usuario
primera_palabra = str(input("Ingrese la primera palabra que desea intercalar ---> "))
segunda_palabra = str(input("Ingrese la segunda palabra que desea intercalar ---> "))

# Condicional para comparar el largo de ambas palabras
if len(primera_palabra) != len(segunda_palabra):
# Mensaje de error si el largo no es igual
    print("Las palabras ingresadas no son del mismo largo.")

# Condicional para combinar ambas palabras
else:
    palabra_intercalada = "".join(i + j for i, j in zip(primera_palabra, segunda_palabra))
    print("La palabra intercalada es:",palabra_intercalada)