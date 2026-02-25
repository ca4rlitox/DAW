"""Crea una matriz de 4×4 con números aleatorios entre 1 y 9.
Luego crea una SEGUNDA matriz llamada matriz_transpuesta que sea la matriz original
 pero con filas y columnas intercambiadas.
Finalmente, imprime ambas matrices."""

import random
matriz=[]
matrizTranspuesta=[]
for i in range(4):
    fila=[]
    for j in range(4):
        fila.append(random.randint(1,9))
    matriz.append(fila)

for fila in matriz:
    for num in fila:
        print(num, end=" ")
    print()
print()

for col in range(4):
    filaTranspuesta = []
    for fila in range(4):
        filaTranspuesta.append(matriz[fila][col])
    matrizTranspuesta.append(filaTranspuesta)

for filaTranspuesta in matrizTranspuesta:
    for num in filaTranspuesta:
        print(num, end=" ")
    print()





