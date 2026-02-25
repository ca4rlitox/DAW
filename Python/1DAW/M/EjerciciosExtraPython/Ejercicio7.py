"""Números mayores que el promedio
Generar una lista de, por ejemplo, 20 números aleatorios entre 1 y 100.
Calcular el promedio de todos los números.
Mostrar solo los números que sean mayores que el promedio."""

import random
suma =0
numeros=[random.randint(1,100) for i in range(0,20)]

for numero in numeros:
    suma=suma+numero

promedio=suma/len(numeros)

for numero in numeros:
    if numero > promedio:
        print(numero,end=" ")