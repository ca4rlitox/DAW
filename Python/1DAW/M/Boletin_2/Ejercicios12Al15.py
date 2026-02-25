import random
"""
12. Realiza un juego en el que debes de acertar un número entre el 1 y el 50 que el
ordenador ha elegido de forma aleatoria. El programa te indicará si has acertado, si te
has pasado o si te has quedado corto. El programa finaliza cuando se acierta o cuando
se superan el número máximo de intentos establecidos en 5.
"""
"""
num=random.randint(1,50)

i=0
for i in range(1,6):
    apuesta = int(input("Apuesta que número es entre el 1 y el 50: "))
    if apuesta==num:
        print("Has acertado")
        break
    elif apuesta>num:
        print("Te has pasado")
    elif apuesta<num:
        print("Te has quedado corto")

"""

"""
13. Modifica el programa anterior para que el programa te de todos los intentos que
necesites pero que cuando aciertes te informe de cuantas veces has fallado antes de
lograrlo
"""
"""
num=random.randint(1,50)
apuesta = int(input("Apuesta que número es entre el 1 y el 50: "))

i=0

while num!=apuesta:
    if num>apuesta:
        apuesta=int(input("Te has quedado corto. Tienes otro intento!"))
    elif num<apuesta:
        apuesta=int(input("Te has pasado. Tienes otro intento!"))
    i+=1

print("Has acertado!")
print("Has fallado ",i," veces")
"""
"""
14. Modifica el programa anterior para que al final del programa te pida si quieres volver
a jugar y en caso afirmativo comience una nueva partida
"""
"""
ingreso=int(input("Para jugar ingresa 1. Para salir cualquier otro. "))

while ingreso==1:
    num=random.randint(1,50)
    apuesta = int(input("Apuesta que número es entre el 1 y el 50: "))

    i=0
    while num!=apuesta:
        if num>apuesta:
            apuesta=int(input("Te has quedado corto. Tienes otro intento!"))
        elif num<apuesta:
            apuesta=int(input("Te has pasado. Tienes otro intento!"))
        i+=1

    print("Has acertado!")
    print("Has fallado ",(i)," veces")

    ingreso=int(input("Para volver a jugar ingresa 1. Para salir cualquier otro. "))
"""
"""
15. Modifica el programa anterior para que al iniciar el juego te pida dos parámetros con
objeto de cambiar la dificultad del juego: el número máximo (antes era siempre 50) o
el número de intentos posibles (antes era siempre 5). 
"""

"""ingreso=int(input("Para jugar ingresa 1.\nPara salir cualquier otro.\n "))

while ingreso==1:
    opcion=int(input("Elije dificultad:\n 1. Para cambiar el rango de posibilidades.\n "
                     "2. Para cambiar los intentos.\n "
                     "3. Para cambiar el rango y los intentos.\n "))
    if opcion==1:
        dificultad=int(input("Elije el rango máximo de posibilidades (entre 1 y ¿...?):\n "))
        num=random.randint(1,dificultad)

        for i in range(1, 6):
            apuesta = int(input("¿Qué número apuestas? Tienes 5 posibilidades: "))
            if apuesta == num:
                print("Has acertado")
                break
            elif apuesta > num:
                print("Te has pasado")
            elif apuesta < num:
                print("Te has quedado corto")

    elif opcion==2:
        dificultad = int(input("Elije el numero de intentos: \n"))
        num = random.randint(1, 50)

        for i in range(1, (dificultad+1)):
            apuesta = int(input("¿Qué número apuestas entre el 1 y el 50?: "))
            if apuesta == num:
                print("Has acertado")
                break
            elif apuesta > num:
                print("Te has pasado")
            elif apuesta < num:
                print("Te has quedado corto")

    elif opcion==3:
        dificultad1=int(input("Elije el rango máximo de posibilidades (entre 1 y ¿...?): "))
        dificultad2 = int(input("Elije el número de intentos: "))
        
    ingreso=int(input("Para volver a jugar ingresa 1. Para salir cualquier otro. "))"""

ingreso = int(input("Este es un juego sencillo en donde tienes que adivinar un número aleatorio "
                    "dentro de un determinado rango,\ntu puedes elegir el rango (entre que números debes adivinar)\n"
                    "y la cantidad de intentos. Buena suerte!\n"
                    "Para jugar ingresa 1.\nPara salir cualquier otro.\n "))

while ingreso == 1:
    opcion = int(input("Elije dificultad:\n Ingresa 1. Para cambiar el rango (entre 1 y el número que elijas).\n "
                               "Ingresa 2. Para cambiar los intentos (entre 1 y el número que elijas).\n "
                               "Ingresa 3. Para cambiar el rango y los intentos.\n "))
    match opcion:

        case 1:
            dificultad = int(input("Elije el rango máximo de posibilidades (entre 1 y ¿...?):\n "))
            num = random.randint(1, dificultad)

            for i in range(1, 6):
                apuesta = int(input("¿Qué número apuestas? Tienes 5 posibilidades: "))
                if apuesta == num:
                    print("Has acertado")
                    break
                elif apuesta > num:
                    print("Te has pasado")
                elif apuesta < num:
                    print("Te has quedado corto")

        case 2:
            dificultad = int(input("Elije el numero de intentos: \n"))
            num = random.randint(1, 50)

            for i in range(1, (dificultad + 1)):
                apuesta = int(input("¿Qué número apuestas entre el 1 y el 50?: "))
                if apuesta == num:
                    print("Has acertado")
                    break
                elif apuesta > num:
                    print("Te has pasado")
                elif apuesta < num:
                    print("Te has quedado corto")

        case 3:
            dificultad1 = int(input("Elije el rango máximo de posibilidades (entre 1 y ¿...?): "))
            dificultad2 = int(input("Elije el número de intentos: "))

            num=random.randint(1,dificultad1)
            for i in range(1, (dificultad2 + 1)):
                apuesta = int(input("¿Qué número apuestas?: "))
                if apuesta == num:
                    print("Has acertado")
                    break
                elif apuesta > num:
                    print("Te has pasado")
                elif apuesta < num:
                    print("Te has quedado corto")

    ingreso=int(input("Para volver a jugar ingresa 1. Para salir cualquier otro. "))
