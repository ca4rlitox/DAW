#Matrices es igual a array, o vectores

matriz=[[2,3],[7,14]]
print(matriz)

print(matriz[0][1]) #accedo a un elemnto de la matriz, 0 es la lista 1 y 1 es el elemento 2 de la lista 1

matriz[0][1]=5 #cambio el valor del elemnto 2 de la lista 1 a 5
print(matriz)

matriz[1]=[14,28] #cambio los valores de la lista 2 (osea la de la posicion 1) por 14 y 28
print(matriz)


#Desempaquetado de una lista
alumno=["Manuel", "Rey",23]
nombre, apellido, edad =alumno #desempaquetado de la lista
print(apellido, nombre, edad)

alumno.reverse() #invierto los elemntos de la lista
print(alumno) #no confundir con sort.reverse() que me lo ordena de manera descendente





