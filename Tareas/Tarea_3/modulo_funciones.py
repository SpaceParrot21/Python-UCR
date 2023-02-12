'''
Este documento contiene todas las funciones matematicas 
requeriadas para la tarea 3
'''


'''Suma'''

# Esta es una funcion para sumar los numeros ingresados por un usuario
# El resultado de la suma se guarda en el file "output_file_suma.txt"

def suma():
    '''Esta es la funcion para sumar'''
    # Crear lista vacia, Solicitar valores al usuario, Almacenar Valores
    lista = []
    sumar = int(input("Ingrese el numero que desea sumar (Ingrese 0 para finalizar):"))
    suma_numeros = 0
    # Agregar los valores ingresado la lista
    while sumar !=0:
        lista.append(sumar)
        sumar = int(input("Ingrese el numero que desea sumar (Ingrese 0 para finalizar):"))
    print("Los numeros ingresados son: ")
    print(lista)
    # Sumar los numero ingresados
    for total in lista:
        suma_numeros += total
    print(f"El total de la suma de {lista} es:")
    print(suma_numeros)
    # Crear documento, escribir resultado y cerrar documento
    output_file = open("output_file_suma.txt", "a")
    output_file.write(f"La suma total de {lista} es: {suma_numeros}\n")
    output_file.close()


'''Resta'''

# Esta es una funcion para restar numeros ingresados por un usuario
# El usuario debe ingresar dos numeros
# El resultado de la suma se guarda en el file "output_file_resta.txt"

def resta():
    '''Funcion para Restar'''
    # Recursividad
    while True:
        # Recibir valores del usuario
        resta_uno = int(input("Ingrese el primer Numero: "))
        resta_dos = int(input("Ingrese el segundo Numero: "))
        # Formula para obtner el resultado
        total = resta_uno - resta_dos
        print(f"El resultado de la resta de ambos valores es: {total}")

        # Crear documento, escribir resultado y cerrar 
        output_file = open("output_file_resta.txt", "a")
        output_file.write(f"El resultado de resta total de {resta_uno} - {resta_dos} es: {total}\n")
        output_file.close() 

        # Verificar si el usuario desea continuar
        continuar = str(input("Indique (Y/N) para realizar otra resta: "))
        continuar = continuar.upper() 
        if continuar == "N":
            print("Gracias!!!")
            break
        else:
            continue


'''Multiplicacion'''

# Esta es una funcion para sumar los numeros ingresados por un usuario
# El resultado de la mulitplicacion se guarda en el file "output_file_multiplicacion.txt"

def multiplicacion():
    '''Esta es la funcion para multiplicar'''
    total = 1
    while True:
        try:
            number = int(input("Ingresa un número y seguiré multiplicando hasta que ingreses 0 para SALIR: \n"))
        # Verificacion del input del usuario
        except ValueError:
            print("Ingrese un numero! Trate nuevamente.")
            continue

        # Verificar si el usuario desea continuar
        if number == 0:
            print(f"El total de la multiplicación es: {round(total)}")
            break
        else:
            total *= number

    # Crear documento, escribir resultado y cerrar 
    output_file = open("output_file_multiplicacion.txt", "a")
    output_file.write(f"El total de multiplicacion es: {total}\n")
    output_file.close()


'''Division'''

# Esta es una funcion para dividir dos numeros ingresados por un usuario
# El usuario debe ingresar dos numeros
# El resultado de la division se guarda en el file "output_file_division.txt"

def division():
    '''Funcion para Dividir'''
    while True:
        # Recibir Numeros enteros del usuario
        primer_numero = int(input("Ingrese el primer numero que desea dividir: "))
        segundo_numero = int(input("Ingrese el segundo numero que desea dividir: "))
        total = primer_numero // segundo_numero
        # Imprimir resultado de la division
        print(f"La division entre ambos numeros es: {total}")

        # Crear documento, escribir resultado y cerrar 
        output_file = open("output_file_division.txt", "a")
        output_file.write(f"El resultado de la division de {primer_numero} // {segundo_numero} es: {total}\n")
        output_file.close()
        continuar = str(input("Indique (Y/N) para continuar: "))
        continuar = continuar.upper()
        if continuar == "N":
            print("\nGracias!")
            break


'''Factorial'''

# Esta es una funcion para obtner el factorial de un numero ingresado por un usuario
# El resultado de la suma se guarda en el file "output_file_factorial.txt"

def factorial():
    '''Funcion para Restar'''
    while True:
        # Recibir numero del usuario y almacenarlo
        num_usuario = int(input("Ingrese un numero positivo entero al que se le va a calcular el factorial: "))
        numero_factorial = 1
        # Verificar que el numero sea entero positivo
        if num_usuario < 0:
            print("---> Se necesita un numero positivo entero (Mayor o igual a ZERO), Inténtalo de nuevo <---")
        elif num_usuario == 0 or num_usuario == 1:
            print("El factorial de ", num_usuario," es", numero_factorial)
        # Operacion para obtener el factorial
        else:
            for i in range(1, num_usuario+1):
                numero_factorial = numero_factorial*i
            print ("El factorial del número",num_usuario,"es",numero_factorial)
             # Crear documento, escribir resultado y cerrar 
            output_file = open("output_file_factorial.txt", "a")
            output_file.write(f"El factorial de {num_usuario} es: {numero_factorial}\n")
            output_file.close()

        # Verificar si el usuario desea continuar
        continuar = str(input("Indique (Y/N) para ingresar un nuevo numero: "))
        continuar = continuar.upper()
        if continuar == "N":
            print("Gracias!!!")
            break
        else:
            continue


'''Potencia'''

# Esta es una funcion para obtner la potencia de un numero elevado a otro.
# Se solicita valores al usuario
# El resultado de la operecion se guarda en el file "output_file_potencia.txt".

def potencia():
    while True:
        # Soilicitar Valores al usuario
        base = int(input("Ingrese el numero base: "))
        exponte = int(input("Ingrese el numero exponente: "))

        # Funcion pow() para obtener la potencia de un numero
        potencia = pow(base, exponte) 
        print(f"El numero {base} elevado al {exponte} es: {potencia}" )

        # Crear documento, escribir resultado y cerrar 
        output_file = open("output_file_potencia.txt", "a")
        output_file.write(f"\nEl numero {base} elevado al {exponte} es: {potencia}\n")
        output_file.close()

        # Verificar si el usuario desea continuar
        continuar = str(input("Indique (Y/N) para continuar: ")) 
        continuar = continuar.upper()
        if continuar == "N":
            print("\nGracias!")
            break
