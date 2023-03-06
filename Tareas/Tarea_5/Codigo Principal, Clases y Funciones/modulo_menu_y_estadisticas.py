'''Este modulo contiene las funciones para el Menu
de usuarios y para mostar estadisticas de los jugadores'''

'''Ambas tareas necesitan de las mismas variables 
Globales para poder operar correctamente'''


# import menu_de_usuarios

# # Importar funcion de estadisticas de los usuarios
# import reading_statistics as r
import clear_terminal as c_terminal
# # Diccionario de usuarios
global USUARIOS
global JUGADOR

USUARIOS = ['Luis', 'John', 'Arturo']
# jugador = []  # Linea original
# JUGADOR = ""
JUGADOR_GLOBAL = []
# TEXT = "".join(JUGADOR_GLOBAL)
# print(JUGADOR_GLOBAL)
print("Usuarios: ", USUARIOS)

# Función principal del menú
def menu_usuarios():
    while True:
        print("Menú de usuarios:")
        print("1. Seleccionar usuario existente")
        print("2. Crear un nuevo usuario")
        print("3. Iniciar juego")
        print("4. Salir")
        opcion = input("\nSelecciona una opción: ")
        c_terminal.clear()
        if opcion == "1":
            seleccionar_usuario()
        elif opcion == "2":
            crear_usuario()
        elif opcion == "3":
            c_terminal.clear()
            if len(JUGADOR_GLOBAL) == 0:
                print("\nAun no ha selecionado ningun usuario!!!\n")
            else:
                break
        elif opcion == "4":
            break
        else:
            print("Opción inválida")


def reading_statistics():

    file_name = "Estadisticas.txt"
# # pRUEBA 
    TEXT = "".join(JUGADOR_GLOBAL)
    try:
        # opening and reading the file 
        file_read = open(file_name, "r")
  
        # search for String Luis
        # text = "Luis"
        # text = JUGADOR
  
        # reading file content line by line.
        lines = file_read.readlines()
  
        new_list = []
        idx = 0
  
        # looping through each line in the file
        for line in lines:
            # if line have the input string, get the index 
            # of that line and put the
            # line into newly created list 
            if TEXT in line:
                new_list.insert(idx, line)
                idx += 1
  
        # closing file after reading
        file_read.close()
  
        # if length of new list is 0 that means 
        # the input string doesn't 
        # found in the text file
        if len(new_list)==0:
            print("\n\"" +TEXT+ "\" is not found in \"" +file_name+ "\"!")
        else:
            # displaying the lines 
            # containing given string
            lineLen = len(new_list)
            print("\n**** Estas son la estadisticas de \"" +TEXT+ "\" ****\n")
            for i in range(lineLen):
                print(end=new_list[i])
            print()
  
    # entering except block
    # if input file doesn't exist 
    except :
        print("\nThe file doesn't exist!")

# # reading_statistics()

# Función para seleccionar un usuario existente
def seleccionar_usuario():
    print("Seleccionar usuario existente")
    if len(USUARIOS) == 0:
        print("No hay usuarios registrados")
    else:
        print("Usuarios:")
        for usuario in USUARIOS:
            print(usuario)
        JUGADOR = input("Selecciona un usuario: ")
        c_terminal.clear()
        if JUGADOR in USUARIOS:
            print("\nHas seleccionado al usuario", JUGADOR,)
            # Mostrar estadisticas del jugador
            JUGADOR_GLOBAL.append(JUGADOR)
            reading_statistics()
            # c_terminal.clear()
            print( "\n---> Selecciona opcion '3' para inicar el juego <---\n")
        else:
            print("Usuario no encontrado")          
            # print("Seleccione la opcion '3' si desea iniciar el juego")
            
# seleccionar_usuario()           

# # def jugador_selecionados():
# #     jugador_selecionado = []
# #     jugador_selecionado.append(jugador)

# Función para crear un nuevo usuario
def crear_usuario(JUGADOR_GLOBAL):
    print("Crear un nuevo usuario")
    nombre = input("Ingresa el nombre del nuevo usuario: ")
    if nombre in USUARIOS:
        print("El usuario ya existe")
    else:   
        USUARIOS.append(nombre)
        print("Usuario creado exitosamente")
        # jugador.append(nombre) # Linea original
        print(USUARIOS)
        print(JUGADOR_GLOBAL)


# # Ejecutar el menú 
menu_usuarios()

