# Ejercicio 5 - Notas de clase

# Descripcion:
# Dado el siguiente diccionario, escriba un programa que
# imprima en pantalla el promedio de notas del estudiante. Debe imprimirlo en
# un diccionario de la forma {"nombre": 75} 

# sampleDict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80,
#             "math": 90
#          }
#       }
#    }
# }

# for key,val in sampleDict.items():
#     total = val * maa
#     print(total,key)


sampleDict = {"class": {"student": {"name": "Mike","marks": {"physics": 70, "history": 80,"math": 90},}}}

print(sampleDict["marks"])

# total = 0

# for i in sampleDict.values():
#     total += i
#     print(total)


# sum = (70 + 80 + 90) / 3
# print(sum)



# d1 = {'a' : 15,'b' : 18,'c' : 20}

# total = 0

# for i in d1.values():
#     total += i

# print(total)