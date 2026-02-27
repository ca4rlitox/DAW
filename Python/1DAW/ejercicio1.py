import random

jugadores = {}
numJugadores = 456
columnas = 12
#El array tiene que empezar en la posicion 1

def inicializaJuego(jugadores,numJugadores):
    for i in range(0,numJugadores):
        jugadores[i] = "Vivo"

def eliminarJugadores(jugadores, numEliminados):
    if numEliminados >= verJugadoresActivos1(jugadores):
        print(f"¡No puedo eliminar a {numEliminados} jugadores! Ahora mismo quedan {numJugadores} activos. ¡Nos quedamos sin ganador!")
    else:
        for i in range(0,numEliminados):
            verificar = False
            afortunado=random.randint(0,455)
            if jugadores[afortunado] == "---":
                while jugadores[afortunado] == "---":
                    afortunado=random.randint(0,455)
            jugadores[afortunado] = "---"
            verificar = True

        print(f"Vamos a eliminar a {numEliminados} jugadores.")
        print(f"Quedan {verJugadoresActivos1(jugadores)} jugadores activos.")

    if verJugadoresActivos1(jugadores) == 1:
        print("Queda solo un jugador activo. Ya tenemos ganador!")

def verJugadoresActivos1(jugadores):
    contador=0
    for i in range(0,numJugadores):
        if jugadores[i] != "---":
            contador+=1
    return contador

def verJugadoresActivos(jugadores):
    contador=0
    for i in range(0,numJugadores):
        if jugadores[i] != "---":
            contador+=1
    print(f"Quedan {contador} jugadores activos!")

inicializaJuego(jugadores,numJugadores)
eliminarJugadores(jugadores,5)
activos = verJugadoresActivos1(jugadores)
print("Jugadores activos:",activos)

