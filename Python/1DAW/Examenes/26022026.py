import random

jugadores = {}
numJugadores = 457
columnas = 12
#El array tiene que empezar en la posicion 1

def inicializaJuego(jugadores,numJugadores):
    for i in range(0,numJugadores):
        jugadores[i] = "Vivo"

def eliminarJugadores(jugadores, numEliminados):
    numJugadores = len(jugadores)
    if numEliminados >= verJugadoresActivos(jugadores):
        print(f"¡No puedo eliminar a {numEliminados} jugadores! Ahora mismo quedan {numJugadores} activos. ¡Nos quedamos sin ganador!")
    else:
        for i in range(0,numEliminados):
            afortunado=random.randint(0,numJugadores)
            if jugadores[afortunado] == "---":
                while jugadores[afortunado] == "---":
                    afortunado=random.randint(0,numJugadores)
            jugadores[afortunado] = "---"


        print(f"Vamos a eliminar a {numEliminados} jugadores.")
        print(f"Quedan {verJugadoresActivos(jugadores)} jugadores activos.")

    if verJugadoresActivos(jugadores) == 1:
        print("Queda solo un jugador activo. Ya tenemos ganador!")

def verJugadoresActivos(jugadores):
    contador=0
    for i in range(0,numJugadores):
        if jugadores[i] != "---":
            contador+=1
    return contador
def verJugadores(jugadores, columnas):
    num = len(jugadores)
    for i in range(1,num):
        if jugadores[i] != "---":
            print(f"|{i}",end="")
        else:
            print("|---|", end ="")
        if i%columnas == 0:
            print("|")

inicializaJuego(jugadores,numJugadores)
eliminarJugadores(jugadores,353)
verJugadores(jugadores,12)
activos = verJugadoresActivos(jugadores)
print("Jugadores activos:",activos)

