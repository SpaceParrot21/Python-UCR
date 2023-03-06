# Diccionario de usuarios
usuarios = {}

# Función para seleccionar un usuario existente
def seleccionar_usuario():
    print("Seleccionar usuario existente")
    if len(usuarios) == 0:
        print("No hay usuarios registrados")
    else:
        print("Usuarios:")
        for usuario in usuarios:
            print(usuario)
        usuario_seleccionado = input("Selecciona un usuario: ")
        if usuario_seleccionado in usuarios:
            print("Has seleccionado al usuario", usuario_seleccionado)
        else:
            print("Usuario no encontrado")

# Función para crear un nuevo usuario
def crear_usuario():
    print("Crear un nuevo usuario")
    nombre = input("Ingresa el nombre del nuevo usuario: ")
    if nombre in usuarios:
        print("El usuario ya existe")
    else:   
        usuarios[nombre]=None
        print("Usuario creado exitosamente")

# Función principal del menú
def menu_usuarios():
    while True:
        print("Menú de usuarios:")
        print("1. Seleccionar usuario existente")
        print("2. Crear un nuevo usuario")
        print("3. iniciar juego")
        print("4.  salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            seleccionar_usuario()
        elif opcion == "2":
            crear_usuario()
        elif opcion == "3":
            break
        elif opcion == "4":
            exit()
        else:
            print("Opción inválida")

# Ejecutar el menú
menu_usuarios()