
"""sudoku = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],

    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],

    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]
"""
import random
sudoku=[]
for i in range(0,9):
    lista=[]
    for j in range(0,9):
        lista.append(random.randint(1,9))
    sudoku.append(lista)

numEnLista=[]
contadorFilas=[]
validadorFilas=0
for lista in sudoku:
    for num in lista:
        contadorFilas.append(lista.count(num))

for n in contadorFilas:
        if n == 1:
            validadorFilas += 1

sudokuColumnas=[]
for columna in range(9):
    col=[]
    for fila in range(9):
        col.append(sudoku[fila][columna])
    sudokuColumnas.append(col)

validadorColumnas=0
contadorColumnas=[]
for columna in sudokuColumnas:
    for num in columna:
        contadorColumnas.append(columna.count(num))

for n in contadorColumnas:
    if n == 1:
        validadorColumnas += 1

if validadorColumnas == 81 == validadorFilas:
    print("Sudoku correcto")
else:
    print("Sudoku incorrecto")



