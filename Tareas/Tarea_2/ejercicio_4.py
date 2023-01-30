# Ejercicio 4 - Lista al cubo

# Descripcion: 
# Escriba un programa que cree una lista de números y la
# imprima. Luego debe imprimir dicha lista pero con cada valor 
# convertido en su cubo.

# Crear una lista
mi_lista = [1, 2, 3, 4]
print(mi_lista)

# Crear una lista para almacenar la raiz cubica de cada numero en la lista 'mi_lista'
raiz_cubica = []
# For loop para interar en cada elemento de la lista y obtener la raiz cubica de cada numero
for i in mi_lista:
    raiz_cubica.append(i*i*i)
print("La raiz cubica de los numero de la lista original son:")
print(raiz_cubica)