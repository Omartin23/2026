print("\033c")

# #Ejemplo 1 Crear una lista de numeros e imprimir el contenido
# numeros=[23,45,23,33,25,100,-100]
# print(numeros)

# lista="["
# for i in range(0,len(numeros)):
#     lista+=f"{numeros[i]} ,"
# print(f"{lista}]")

# lista="["
# i=0
# while i<len(numeros):
#     lista+=f"{numeros[i]} ,"
#     i+=1
# print(f"{lista}]")

# #Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
# palabras=["Hola","NBA","Ganador","Perdedor"]
# palabraBuscar=input("Palabra a buscar: ")

# if palabraBuscar in palabras:
#     print("Yessirrr")
# else: 
#     print("Yessirrrn't")



# #2DA FORMA
# palabras=["Hola","NBA","Ganador","Perdedor"]
# palabraBuscar=input("Palabra a buscar: ")

# coincidencia=False
# for i in palabras:
#     if i==palabraBuscar:
#         coincidencia=True
        
# if coincidencia:
#  print(f"Se encuentra en la lista")
# else:
#  print(f"No esta en la lista")    

 

# #3er FORMA
# coincidencia=False
# i=0
# while i<len(palabras):
#    busqueda=palabraBuscar in palabras
#    if busqueda:
#       coincidencia=True
#    i+=1

# if coincidencia:
#  print(f"Se encuentra en la lista")
# else:
#  print(f"No esta en la lista")   



#Ejemplo 3 Añadir elementos a la lista
# lista=[]
# true="S"
# while true=="S":
#   lista.append(input("Valor a agregar: ").upper().strip())
#   true=input("Desea agregar otro valor? (S/N)").upper().strip()
  

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda

agenda=[
         ["Carlos", "6181234567"],
         ["Juan", "2334567"],
         ["Tony", "2342323"]
       ]

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])

lista=""
for r in range(0,3):
    for c in range(0,2):
        lista+=f"{agenda[r][c]}, "
    lista+="\n"
print("["+lista+"]")


# lista="["
# for i in range(0,len(numeros)):
#     lista+=f"{numeros[i]} ,"
# print(f"{lista}]")