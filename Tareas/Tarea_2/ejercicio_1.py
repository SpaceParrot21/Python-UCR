# Ejercicio 1 - Factorial del número dado
# Descripcion: 

# Escriba un programa en el que dado un número
# por el usuario, imprima el factorial (!) de dicho número


# Solicitar un numero entero positivo al usuario
num_usuario = int(input("Ingrese un numero positivo entero al que se le va a calcular el factorial: "))

# Variable del factorial
factorial = 1

# Mensaje de error si numero es menor a 0
if num_usuario < 0:
    print("---> Se necesita un numero positivo entero (Mayor o igual a ZERO), ejecute el codigo nuevamente y ingrese un numero <---")
# Condicion si el numero es 0 o 1 mostrar que el factorial es 1.

elif num_usuario == 0 or num_usuario == 1:
    print("El factorial de ", num_usuario," es", factorial)

# Condicion con calculo matematico para obtener el numero factorial del numero ingresado por el usuario
else:
    for i in range(1, num_usuario+1):
        factorial = factorial*i
    print ("El factorial del número",num_usuario,"es",factorial)