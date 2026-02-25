#TUPLAS

tupla1 = (1, 2, 3)
tupla2 = ("Helena", "Jorge", "Ana")
tupla3 = ("Manuel", True,30,1200.45) #son heterogeneas pero no se pueden modificar, ni añadir, ni quitar
lista1=[45.33, 67.33, 1200.44]

""" tupla2[1]="Antonia" """#me da un error porque no se puede modificar

#Puedo usar todas las funciones de las listas que no modifiquen el contenido
#como por ejemplo list(), tuple() (para convertir a tupla) str()

tupla4 = tuple(lista1)#convierto la lista en una tupla y ahora no la puedo modificar
print(tupla4)

lista2 = list(tupla2)#convierto la tupla en una lista y ahora si puedo modificarla
print(lista2)

texto=str(tupla3)#contvierto la tupla en un string
print(texto[1:-1])#imprimo la cadena sin los corchetes

tuplaVacia = ()#tupla vacia (no tiene mucha utilidad)

tuplaConUnElemento = ("Manuel",)#creo unatupla con un unico elemento agregando una , al final






