import random
matriz=[]
for i in range(3):
    fila=[]
    for j in range(4):
        fila.append(0)
    matriz.append(fila)

for _ in range(3):
    fila_random=random.randint(0,3)
    columna_random=random.randint(0,3)
    while(matriz[fila_random][columna_random]=='X'):
        fila_random=random.randint(0,3)
        columna_random=random.randint(0,3)

    matriz[fila_random][columna_random]='X'
contador=0
for fila in matriz:
    for num in fila:
        if num=='X':
            contador+=1
        print(num,end=" ")
    print()

print(f"cantidad de 'X'={contador}")
