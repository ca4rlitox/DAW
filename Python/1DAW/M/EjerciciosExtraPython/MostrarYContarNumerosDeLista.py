"""Contar cuántas veces aparece cada número en una lista
Generá una lista de 15 números aleatorios entre 1 y 10.
Mostrás cuántas veces aparece cada número.
Solo mostrar los números que realmente aparezcan (no mostrar “0 veces”)."""

import random
lista=[random.randint(1,10) for i in range(15)]
numerosRepetidos=[]
contador=[]
for numero in lista:
    if numero not in numerosRepetidos:
        numerosRepetidos.append(numero)
        contador.append(lista.count(numero))
print(f"la lista es {lista}")
for i in range(0,len(numerosRepetidos)):
    if contador[i]==1:
        print(numerosRepetidos[i], " se repite ", contador[i]," vez")
    elif contador[i]>1:
        print(numerosRepetidos[i], " se repite ", contador[i]," veces")

