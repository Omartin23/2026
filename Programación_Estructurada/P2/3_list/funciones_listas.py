"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""

print("\033c")
#Funciones más comunes en las listas
paises=["México", "Canadá", "EUA", "Mexico", "Brasil"]
numeros=[23,45,8,24]
varios=[33,3.1416,"hola",True]
vacio=[]

#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)
print(vacio)
print(paises[0]+" "+paises[3])

#Recorrer la lista 
#1er forma 
for i in paises:
    print(i)

#2do forma 
for i in range(0,len(paises)):
    print(paises[i])


#ordenar elementos de una lista
paises=["México", "Canadá", "EUA", "Mexico", "Brasil"]
print(paises)

paises.sort()
print(paises)


#dar la vuelta a una lista
paises.reverse()
print(paises)


#Agregar, insertar, Añadir un elemento a una lista
paises=["México", "Canadá", "EUA", "Mexico", "Brasil"]
print(paises)
#1er forma 
paises.append("Honduras")
print(paises)

#2da forma
paises.insert(1,"Argentina") 
print(paises)
paises.insert(100,"Panamá")
print(paises)

#Eliminar, borrar, suprimir, un elemento de una lista
#1er forma
paises.pop(4)
print(paises)


#2da forma 
paises.remove("EUA")
print(paises)

#Buscar un elemento dentro de la lista
buscar="Brasil" in paises
if buscar==True:
    print("Yessirrr")
else:
    print("Bruh")

#Contar el numeros de veces que aparece un elemento dentro de una lista
numeros=[23,45,24,8,23,50,23]
numContar=int(input("Número a contar: "))
num=numeros.count(numContar)
print(f"El número aparece {num} veces")


#Conocer la posicion o indice en el que se encuentra un elemento de la lista
numPosicion=int(input("De que número quiere saber la posición: "))
posicion=numeros.index(numPosicion)
print(f"Posición {posicion}")

#Unir el contenido de una lista dentro de otra lista
numeros1=[23,45,24,8,23,50,23]
print(numeros1)
numeros2=[100,-100]
print(numeros2)

numeros1.extend(numeros2)
print(numeros1)

#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenido ordenado descendentemente
numeros1.sort()
numeros1.reverse()
print(numeros1) 

