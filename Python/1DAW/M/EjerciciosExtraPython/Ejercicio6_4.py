"""Crear una matriz 5×5 con números aleatorios entre 1 y 9
Mostrar la matriz
Contar cuántos números son mayores que 5
Mostrar el total"""

import random
contador=0
matriz=[]
for _ in range(5):
    fila=[]
    for _ in range(5):
        fila.append(random.randint(1,9))
    matriz.append(fila)
    for num in fila:
        if num>5:
            contador+=1
        print(num, end=" ")
    print()
print(f"hay {contador} números mayores a 5")
