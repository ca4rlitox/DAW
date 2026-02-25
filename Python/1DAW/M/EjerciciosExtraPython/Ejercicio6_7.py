import random

matriz=[]
for i in range(5):
    fila=[]
    for j in range(5):
        fila.append(0)
    matriz.append(fila)

for _ in range(5):
    fila_random=(random.randint(0,4))
    columna_random=(random.randint(0,4))

    while matriz[fila_random][columna_random] == 'X':
        fila_random=(random.randint(0,4))
        columna_random=(random.randint(0,4))

    matriz[fila_random][columna_random]='X'

contadorMinas =0

for fila in matriz:
    for num in fila:
        nums=str(num)
        print(nums.replace('0','-'),end=' ')
        if num =='X':
            contadorMinas+=1
    print()

contadorPorFilas=0
for i,j in enumerate(matriz):
    for num in j:
        if num == 'X':
            contadorPorFilas+=1
    if contadorPorFilas==1:
        print("En la fila ", i," hay ",contadorPorFilas," mina")
    else:
        print("En la fila ", i," hay ",contadorPorFilas," minas")
    contadorPorFilas=0


