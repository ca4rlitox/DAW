"""Vamos a hacer una implementación del juego del buscaminas y lo primero es preparar el
tablero. Genera un array de dos dimensiones de 5 filas por 5 columnas. El tablero
tendrá 5 minas que se colocaran de forma aleatoria en cinco posiciones del array. Las
minas se representarán con un 1 y las posiciones sin mina con un 0."""
"""Modifica tu programa para que le puedas decir por teclado el tamaño del tablero de
juego (siempre será cuadrado, así que solo le dirás un número entero) y el número de
minas. Comprueba que no se pueden poner mas minas que las posiciones del tablero
(en un tablero de 3x3 no puede haber 10 minas, por ejemplo"""

import random
tamanio=int(input("Ingresa el tamaño que quieres que tenga el tablero: "))
minas=int(input("Ingresa la cantidad de minas que quieres que haya: "))
while minas>tamanio*tamanio:
    minas=int(input("Cantidad de minas elevada vuelve a ingresar: "))
tablero=[]

for i in range(tamanio):
    fila=[]
    for j in range(tamanio):
        fila.append(0)
    tablero.append(fila)

for _ in range(minas):   # repetimos 5 veces
    fila_random = random.randint(0, tamanio-1)
    col_random = random.randint(0, tamanio-1)

    while tablero[fila_random][col_random] == 1:
        fila_random = random.randint(0, tamanio-1)
        col_random = random.randint(0, tamanio-1)

    tablero[fila_random][col_random] = 1

for fila in tablero:
    for numero in fila:
        print(numero,end=" ")
    print()


