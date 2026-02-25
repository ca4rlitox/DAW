"""Realiza un juego en el que debes de acertar un número entre el 1 y el 50 que el
ordenador ha elegido de forma aleatoria. El programa te indicará si has acertado, si te
has pasado o si te has quedado corto. El programa finaliza cuando se acierta o cuando
se superan el número máximo de intentos establecidos en 5. """

import random

def genaraNumero():
    num=random.randint(1,50)
    return num

def comprobar_intento(numero_secreto,numero_usuario):

    if numero_usuario == numero_secreto:
        return "acierto"
    elif numero_usuario > numero_secreto:
        return "alto"
    else:
        return "bajo"

def jugar():
    num=genaraNumero()
    intentos=0
    while intentos!=5:
        num_usuario = int(input("Ingresa un número"))
        resultado=comprobar_intento(num, num_usuario)

        if resultado=="acierto":
            print("Has acertado")
            return
        elif resultado=="alto":
            print("Te has pasado")
        else:
            print("Te has quedado corto")
        intentos+=1
    print("Te has quedado sin intentos")

jugar()



