# Calculadora Matematica

'''Esta calculadora es capaz de: 
- Sumar entre n numeros
- Restar entre 2 numeros
- Multiplicar entre n numeros
- Divir entre 2 numeros
- Obtener el Factorial de 1 numero
- Obtener la Potencia 1 numero elevado al otro
'''

# INICIA MENU

menu = {}
menu['2']="Resta"
menu['3']="Multiplicación"
menu['7']="SALIR"
menu['1']="Suma"
menu['5']="Factorial"
menu['6']="Potencia"
menu['4']="División"

while True:
    # Odernar y imprimir opciones del menu
    print("\n<--- Menu de Opciones --->")
    options=menu.keys()
    for entry in sorted(options):
        print (entry, menu[entry])

    # Selecionar opcion
    selection=input("Please Select:")

    # Opcion seleccionada y invovacaion de funciones
    if selection =='1':
        import modulo_funciones
        modulo_funciones.suma()
    elif selection == '2': 
        import modulo_funciones
        modulo_funciones.resta()
    elif selection == '3':
        import modulo_funciones
        modulo_funciones.multiplicacion()
    elif selection == '4':
        import modulo_funciones
        modulo_funciones.division()
    elif selection == '5':
        import modulo_funciones
        modulo_funciones.factorial()
    elif selection == '6':
        import modulo_funciones
        modulo_funciones.potencia()
    elif selection == '7':
        print("Muchas Gracias! \n")
        break
    else:
        print ("\n Opción no válida \n" )
