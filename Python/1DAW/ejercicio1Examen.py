import random

jugadores = {}
numJugadores = 456
columnas = 12

def inicializarJuego(jugadores,numJugadores):
    for i in range(0,numJugadores):
        jugadores[i] = "Vivo"

def eliminarJugador(jugadores,eliminarJugadores):
    if eliminarJugadores >= len(jugadores):
        print(f"¡No pueden estar todos muertos!. Hay {len(jugadores)} jugadores y ¡Pretendes matar a {eliminarJugadores} jugadores!")
    else:
        for i in range(0,len(jugadores)):
            afortunado = random.randint(0,numJugadores)
            if jugadores[afortunado] == "Inactivo":
                while jugadores[afortunado] == "Inactivo":
                    afortunado = random.randint(0,numJugadores)
            jugadores[afortunado] = "Inactivo"
def verJugadoresActivos(jugadores):
    vivos=0
    for i in range(0,len(jugadores)):
        if jugadores[i] != "Inactivo":
            vivos+=1
    return vivos


inicializarJuego(jugadores,456)
eliminarJugador(jugadores,400)
print(verJugadoresActivos(jugadores))
