#MODIFICAR LISTAS
#APPEND
"""enteros = [1, 2, 3, 2]

enteros.append(33) #añade un elemento al final del vector

print(enteros)

enteros.insert(2, 777) #inserta un elemento delante de la posicion indicada, primero la posicion y luego el valor a insertar

print(enteros)

#CONCATENAR
masEnteros = [34, 35, 36]
todosJuntos = masEnteros+enteros #podemos concatenar listas, no crea una nueva lista con todos los enteros
print(todosJuntos)

masEnteros.extend(enteros) #concatena los enteros al final de la lista de masEnteros
print(masEnteros)

#ELIMINAR ELEMENTOS DE LA LISTA

#POP
numero= todosJuntos.pop() #pop() sin argumentos, elimina el utlimo elemento de la lista y lo devulve
print(todosJuntos)
print(numero) #imprime el valor del utlimo elemento de la lista que habiamos quitado

numero= todosJuntos.pop(2) #pop() con argumentos, elimina el elemento de la posicion indicada y lo devulve
print(todosJuntos)
print(numero) #imprime el valor del elemento de la posicion indicada que habiamos quitado

#CLEAR
todosJuntos.clear() #limpia la lista
print(todosJuntos)

#REMOVE

todosJuntos.remove(3) #remueve el elemento indicado, no el de la posicion (busca que haya un 3 en la lista y lo elimina)
                        #cuando el elemento esta repetido elimina el primero que aparece en la lista
                        #si no lo encuentra da error (exception)"""
#ORDENAR LISTAS
#SORT
"""enteros =[1,22,3,12]
masEnteros=[61,33,7,13,8]
todosJuntos = masEnteros + enteros
print(todosJuntos)
todosJuntos.sort() #ordena la lista, siempre y cuando los elementos coincidan con el tipo de dato
print(todosJuntos)

todosJuntos.sort(reverse=True) #ordena la lista en reversa
print(todosJuntos)  """

"""nombres =["Manuel", "pepe", "Luis", "Maria"]
nombres.sort() #ordena la lista alfabeticamente, pero las minusculas iran despues de las mayusculas
print(nombres)


nombres.sort(reverse=True)
print(nombres)"""

#COMPROBAR EXISTENCIA DE UN ELEMENTO EN UNA LISTA
nombres =["Manuel", "pepe", "Luis", "Maria"]

"""if "pepe" in nombres: #compruebo si el nombre pepe se encuntra en la lista nombres
    print("pepe si se encuntra en la lista")
else:
    print("pepe no se encuntra en la lista")

#COMPROBAR QUE UN ELEMENTO NO EXISTE EN UNA LISTA
if "ana" not in nombres: #compruebo si el nombre ana no se encuntra en la lista nombres
    print("ana no se encuntra en la lista")
else:
    print("ana si se encuntra en la lista")


#ENCONTRAR LA POSICION DE UN ELEMENTO EN UNA LISTA
posicion = nombres.index("Luis") #index() devulve la posicion de un elemento en la lista
print("Luis se encuntra en la posicion", posicion)
                                #si el elemento no se encuntra en la lista da error (exception)

#conviene preguntar antes si esta con un if
if "Luis" in nombres:
    posicion = nombres.index("Luis")
    print("Luis se encuntra en la posicion", posicion)
else:
    print("Luis no se encuntra en la lista")

#CONTAR NUMERO DE VECES DE UN ELEMENTO EN UNA LISTA
#COUNT
veces = nombres.count("Luis")
print("Luis se repite",veces,"veces en la lista")

#si el elemento no se encuntra en la lissta con index devuelve cero
veces = nombres.count("ana")
print("ana se repite",veces,"veces en la lista")"""








