"""Genera 50 números aleatorios entre 10 y 100. Muestra:
    -La lista completa
    -La suma de todos los números
    -El promedio
    -Cuántos números están por encima del promedio"""

import random
contador=0

numAleatorios=[random.randint(10,100) for i in range(1,51)]

print("Lista de números aleatorios:",numAleatorios)
print("Suma de todos los números de la lista:",sum(numAleatorios))
promedio=sum(numAleatorios)/len(numAleatorios)
print("Promedio de los números de la lista:",round(promedio,2))

for numeros in numAleatorios:
    if numeros>promedio:
        contador+=1

print("Números de la lista que superan el promedio:",contador)