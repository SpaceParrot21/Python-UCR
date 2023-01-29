# Ejercicio 2 - Triángulo: 
# Descripcion:  

# Este programa recibe un numero del usuario y despliegua 
# en pantalla el siguiente patrón en triangulo de números 
# llegando hasta el número elegido.

# Mensaje de error si el dato ingresado no es un numero
while True:
    try:
        num_usuario = int(input("Ingrese un number: "))
        break
    except ValueError:
        print("\nEsto no es un numero. Trate nuevamente...")        

if num_usuario <= 1:
    print("El numero ingresado debe ser mayor a 1.")
else:
    for x in range(1, num_usuario+1): # Varaible x desde 1 a numero ingresado por el usuario
        for i in range(1, x+1): # Variable i desde 1 hasta x
            print(i , end=" ") # Imprime variable i con espacio
        print("") # Este es un salto de linea por defecto
