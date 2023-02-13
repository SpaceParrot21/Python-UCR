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
    print(f"La cantidad de letras es: {letras}")
    print(f"La cantidad de numeros es: {numeros}")
    print(f"La cantidad de caracteres especiales es: {caracteres_especiales}")
    return numeros, letras, caracteres_especiales

#Invocacion de la funcion y casos de prueba
conteo_letras_numeros_caracteres("P@#yn26at^&i5ve")
# conteo_letras_numeros_caracteres("Querty-21")
# conteo_letras_numeros_caracteres("Pyl@nc'3r-23")
# conteo_letras_numeros_caracteres("Prueba4_56")
# conteo_letras_numeros_caracteres("asdf4534")
