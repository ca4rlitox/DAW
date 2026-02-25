#CONJUNTOS
#son modificable, no tienen orden (no puedo recuperarlos por el elemento que ocupa), y no permiten duplicados

#tiene implementado operaciones para hacer conjuntos (union, intersecciones, etc)
#puedo identificar por ejemplo si un elemento se encuentra en un conjunto y en otro no, o si se encuentra en los dos

conjunto1={"Ana","Pedro","Juan","Pablo","Maria"} #utiliza llaves
conjunto2={1,33,56,7,9,1,33,2,33,4,2,5,33,5,3,1,3,33}
print(conjunto1)
print(conjunto2)

"""print(conjunto1[2])""" #me da un error porque no se pueden acceder por el index

conjunto3={1,5,7,4,7,5,3,1,7,9}
print(conjunto3)#los duplicados se quitan

#La palabra reservada para los conjuntos es set()

#Eliminar un elemento del conjunto
#REMOVE
conjunto1.remove("Pedro") #Lo elimina si el elemnto existe, sino da error
print(conjunto1)

#DISCARD
conjunto1.discard("Ana") #Lo elimina si el elemnto existe, sino no da error

#POP -- elimina un elemento aleatorio (elimina el primero, pero como es aleatorio puede ser cualquiera)
print(conjunto1)
conjunto1.pop()
print(conjunto1)

#CLEAR -- elimina todos los elementos del conjunto y devuelve un conjunto vacio
print(conjunto1)
conjunto1.clear()
print(conjunto1)

#CONVERTIR LISTA EN CONJUNTO para eliminar duplicados
lista1=[1,33,56,7,9,1,33,2,33,4,2,5,33,5,3,1,3,33]
conjunto4=set(lista1)
lista2=list(conjunto4)
print(conjunto4)