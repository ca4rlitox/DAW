"""Construir una lista de 10 números aleatorios entre 1 y 50 sin repetir"""
import random

numeros = set() #me crea un conjunto vacio
while len(numeros) < 10: #hay que hacerlo de esta manera para asegurarnos que sean 10 números, sino los repetidos los quita y con un for puede dar menos
    numeros.add(random.randint(1, 50)) #la funcion para agregar un elemento a un set es add() y no append()

print(list(numeros))

#Se puede recorrer el conjunto pero los recorrera de manera desordenada