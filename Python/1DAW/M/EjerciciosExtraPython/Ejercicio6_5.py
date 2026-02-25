"""Crear una matriz 4×4 con números aleatorios entre 1 y 9
Mostrar la matriz
Calcular la suma de cada columna
Mostrar las sumas,"""

import random

matriz=[]
columnas=[]
for i in range (4):
    fila=[]
    for j in range (4):
        fila.append(random.randint(1,9))
    matriz.append(fila)

for fila in matriz:
    for num in fila:
        print(num,end=" ")
    print()

for col in range(4):
    suma=0
    for fila in range(4):
        suma=suma+matriz[fila][col]
    print(suma)
