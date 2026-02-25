""" Queremos hacer el juego de piedra, papel o tijera. El usuario juega contra el ordenador y tiene
que decirnos si gana, pierde o empata. Gana el primero (ordenador o humano) que consigue
tres victorias. Hazlo de forma modular"""

import random

def ganaOrdenador(ordenador,usuario):
    if ordenador=="piedra" and usuario=="tijera":
        return True
    if ordenador=="tijera" and usuario=="papel":
        return True
    if ordenador=="papel" and usuario=="piedra":
        return True
    return False

def ganaUsuario(ordenador,usuario):
    if usuario=="piedra" and ordenador=="tijera":
        return True
    if usuario=="tijera" and ordenador=="papel":
        return True
    if usuario=="papel" and ordenador=="piedra":
        return True
    return False

def ganoPartidaUsuario(ganoUsuario,empate):
    if ganoUsuario>=2:
        return True
    if ganoUsuario==1 and empate==2:
        return True
    return False

def ganoPartidaOrdenador(ganoOrdenador,empate):
    if ganoOrdenador>=2:
        return True
    if ganoOrdenador==1 and empate==2:
        return True
    return False

def huboEmpate(ganoOrdenador,ganoUsuario,empate):
    if empate==1 and ganoUsuario==1 and ganoOrdenador==1:
        return True
    return False
    

def batalla():
    piePapOTij = ("piedra", "papel", "tijera")
    ganoUsuario=0
    ganoOrdenador=0
    empate=0
    for i in range (3):
        ordenador = piePapOTij[random.randint(0, 2)]
        usuario = input("piedra, papel o tijera: ")
        print("Ordenador: ", ordenador)
        if ganaOrdenador(ordenador,usuario):
            ganoOrdenador+=1
            print("Ordenador gana esta batalla")
        elif ganaUsuario(ordenador,usuario):
            ganoUsuario+=1
            print("Usuario gana esta batalla")
        else:
            empate+=1
            print("empatan esta batalla")

    if ganoPartidaUsuario(ganoUsuario,empate) :
        print("El usuario gana!")
    elif ganoPartidaOrdenador(ganoOrdenador,empate):
        print("El ordenador gana!")
    else:
        print("Hay empate!")


batalla()


