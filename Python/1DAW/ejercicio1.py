import random

jugadores = {}
numJugadores = 456
columnas = 12
#El array tiene que empezar en la posicion 1

def inicializaJuego(jugadores,numJugadores):
    for i in range(0,numJugadores):
        jugadores[i] = "Vivo"

def eliminarJugadores(jugadores, numEliminados):
    if numEliminados >= verJugadoresActivos(jugadores):
        print(f"¡No puedo eliminar a {numEliminados} jugadores! Ahora mismo quedan {verJugadoresActivos(jugadores)} activos. ¡Nos quedamos sin ganador!")
    else:
        for i in range(0,numEliminados):
            verificar = False
            afortunado=random.randint(0,len(jugadores))
            if jugadores[afortunado] == "---":
                while jugadores[afortunado] == "---":
                    afortunado=random.randint(0,len(jugadores))
            jugadores[afortunado] = "---"
            verificar = True

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

inicializaJuego(jugadores,5000)
eliminarJugadores(jugadores,555)
activos = verJugadoresActivos(jugadores)
print("Jugadores activos:",activos)

