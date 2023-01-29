factorial = 1

f = int(input("Ingrese un número al que se le va a calcular el factorial:   "))

for x in range (1,f+1):

    factorial = factorial * x

 

print (" El factorial del número",f," ", "es",factorial)