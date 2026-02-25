"""Pide al usuario un número y crea un array de enteros de tantas posiciones como indique
ese número. Rellénalo con números aleatorios entre el 10 y el 1000 y finalmente
pregunta al usuario por la posición de la que quiere recuperar el valor. El programa
mostrará el número de la posición indicada si esta existe y un error si tratamos de
recuperar una posición que no existe (menor a 0 o mayor a la longitud del array)
"""
import random

num=int(input("Ingresa un número"))

numeros=[random.randint(10,1000) for i in range(num)]

numARecuperar=int(input("Ingrese la posicion que quiere recuperar el valor"))
print(numeros)
if numARecuperar<0 or numARecuperar>len(numeros)-1:
    print("La posicion no existe")

else:
    print(numeros[numARecuperar])