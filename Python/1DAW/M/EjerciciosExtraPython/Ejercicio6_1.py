"""Crea una matriz de 3 filas y 3 columnas, donde cada elemento sea 0.
Luego imprime la matriz fila por fila, así:

0 0 0
0 0 0
0 0 0"""

"""matriz=[]
for i in range(3):
    fila=[]
    for j in range(3):
        fila.append(0)
    matriz.append(fila)
    filaTexto=str(fila)
    filaTexto=filaTexto.replace("[","")
    filaTexto=filaTexto.replace("]","")
    filaTexto=filaTexto.replace(",","")
    print(str(filaTexto),end="")
    print()"""

"""matriz=[]
for i in range(3):
    fila=[]
    for j in range(3):
        fila.append(0)
    matriz.append(fila)
    for num in fila:
        print(num,end=" ")
    print()"""

"""A partir de la matriz anterior:
    -Coloca un 1 en una posición aleatoria de la matriz
    -Imprimí la matriz para ver dónde cayó"""

import random
contadorCeros=0
matriz=[]
for i in range(3):
    fila=[]
    for j in range(3):
        fila.append(0)
    matriz.append(fila)

for _ in range(3):
    fila_random=random.randint(0,2)
    columna=random.randint(0,2)

    while matriz[fila_random][columna]==1:
        fila_random=random.randint(0,2)
        columna=random.randint(0,2)

    matriz[fila_random][columna]=1

for fila in matriz:
    for num in fila:
        if num==0:
            contadorCeros+=1
        print(num,end=" ")
    print()
print(f"Cantidad de ceros: {contadorCeros}")

