jugador1=True
jugador2=False
turno='X'

k = 1
print("-------------")
for i in range(3):
    for j in range(3):
        print("|", end="")
        print(" ", k, " ", end="", sep="")
        k += 1
    print("|\n-------------")

for i in range(1,10):
    movimientoJug1=int(input("Jugador 1(X): "))

    if jugador1==True:
        turno='O'
        jugador1=False
    else:
        turno='X'

    movimiento=[]
    for j in range(3):
        fila=[]
        for k in range(3):
            fila.append(turno)
        movimiento.append(fila)


    """print("-------------")
    for _ in range(3):
        for j in range(3):
            print("|", end="")
            print(" "," "," ", end="", sep="")
        print("|\n-------------")"""


"""    print("-------------")
    for j in range(3):
        fila=[]
        for k in range(3):
            fila.append(int(input("jugador 1(X): ")))
            print("|", end="")
            
            print(" ", " ", " ", end="", sep="")
        movimiento.append(fila)
        print("|\n-------------")"""