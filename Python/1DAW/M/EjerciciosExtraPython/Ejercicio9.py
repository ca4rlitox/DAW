"""Escribe un programa que genere 100 números aleatorios comprendidos entre el 1 y 50
(ambos inclusive) y, posteriormente, obtenga el mayor, el menor y el que mas veces se
repite (y nos diga cuantas veces lo hace).
"""

import random

numeros=[random.randint(1,50) for i in range(10)]
print(numeros,end=" ")
masRepetido=0
cantidadRepetido=0
for numero in numeros:
    num=numeros.count(numero)
    if num>cantidadRepetido:
        masRepetido=numero
        cantidadRepetido=num

print()
print("El que mas se repite es el ",masRepetido,". Se repite ",cantidadRepetido," veces.")



