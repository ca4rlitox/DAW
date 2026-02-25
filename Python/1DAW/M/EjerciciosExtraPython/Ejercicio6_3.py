"""Crear una matriz 3×4 llena de números aleatorios entre 1 y 9
Mostrar la matriz en pantalla
Luego, imprimir la suma de cada fila"""

import random
matriz=[]
sumas=[]
for i in range (3):
    fila=[]
    for j in range(4):
        fila.append(random.randint(1,9))
    matriz.append(fila)
    for num in fila:
        print(num,end=" ")
    sumas.append(sum(fila))
    print()

for i,s in enumerate(sumas):
    print(f"la suma de la fila {i+1} es {s}")


