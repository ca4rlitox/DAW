tablero = [0,0,0,0,0,0,0,0,0]

def verTablero():

    print("|-----------|")
    print("|",circuloOequis(tablero[0]),"|",circuloOequis(tablero[1]),"|",circuloOequis(tablero[2]),"|")
    print("|-----------|")
    print("|",circuloOequis(tablero[3]),"|",circuloOequis(tablero[4]),"|",circuloOequis(tablero[5]),"|")
    print("|-----------|")
    print("|",circuloOequis(tablero[6]),"|",circuloOequis(tablero[7]),"|",circuloOequis(tablero[8]),"|")
    print("|-----------|")

def movimientoValido(pos):
    if pos >= 9 or pos < 0 or tablero[pos] != 0:
        return False
    else:
        return True

def circuloOequis(caracter):
    if caracter == 1:
        return "X"
    elif caracter == 2:
        return "O"
    else:
        return " "

def juegaJugador1():
    ficha = int(input("Jugador 1, te toca"))
    if not movimientoValido(ficha):
        while not movimientoValido(ficha):
            ficha = int(input("Ficha introducida erronea. Intentalo otra vez."))
    tablero[ficha] = 1
    verTablero()

def juegaJugador2():
    ficha = int(input("Jugador 2, te toca"))
    if not movimientoValido(ficha):
        while not movimientoValido(ficha):
            ficha = int(input("Ficha introducida erronea. Intentalo otra vez."))
    tablero[ficha] = 2
    verTablero()

def ganaJugador1():
    if tablero[0] and tablero [4] and tablero[8]:
        return True
    if tablero[2] and tablero[4] and tablero[6]:
        return True
    return False

def quedanMovimientos():
    k=0
    for i in tablero:
        if tablero[i] != 0:
            k+=1
    return k < 9

def main():
    while quedanMovimientos():
        verTablero()
        juegaJugador1()
        if not quedanMovimientos():
            print("No quedan movimientos. La partida queda en tablas.")
            break
        juegaJugador2()
        if not quedanMovimientos():
            print("No quedan movimientos. La partida queda en tablas.")
            break



main()