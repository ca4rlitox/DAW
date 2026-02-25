nombres =["Manuel", "pepe", "Luis", "Maria"]
numeros=[23,14.5,7,123,5,67]

print(numeros[2:4]) #cogemos un subconjuto de la lista de los elemntos en la posicion 2 y 3

listaNueva = numeros[3:] #creo una lista nueva a partir de los elemntos de la lista original
print(listaNueva)

otraLista = numeros[-3:-1] #tambien se puede hacer con indices negatios
print(otraLista)

listaAlreves = numeros[-1::-1] #creo una lista al reves
print(listaAlreves)