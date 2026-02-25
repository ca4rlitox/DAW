"""Escribe un programa que lea una hora por teclado en formato 24 horas (HH:MM).
Tu programa debería de decir si corresponde a la mañana (entre las 6 y las 11, ambas
inclusive), si es una hora de la tarde (entre las 12 y las 19, ambas inclusive),
si es de la noche (entre las 20 y las 23, ambas inclusive), si es de la madrugada
(entre las 0 y las 5,ambas inclusive) o bien, si el formato no es correcto o
no se corresponde con una hora real (minutos de mas de 60, horas negativas o
por encima de 23, etc). No tienes que contemplar mas errores que los de este tipo
Ejemplos de ejecución:
Introduce una hora: 25:70
No es una hora válida
Introduce una hora: 13:35
Son las 13:35 de la tarde
"""

hora = input("Introduce una hora en formato 24 horas (HH:MM) ")
# hora="6:50pm"
dosPuntos = hora.index(':')
horas = hora[:dosPuntos]
minutos = hora[dosPuntos + 1:]
# ampm=hora[-2:]
print(minutos)

"""if "am"==ampm=="pm":
    minutos=hora[dosPuntos+1:-2]
    if 1 <= int(horas) <= 12 and 60 > int(minutos) >=0:
        if"""
if 0 <= int(horas) <= 23 and 60 > int(minutos) >= 0:
    if 6 <= int(horas) <= 11:
        print("Son las ", horas, ":", minutos, " de la mañana", sep="")
    elif 12 <= int(horas) <= 19:
        print("Son las ", horas, ":", minutos, " de la tarde", sep="")
    elif 20 <= int(horas) <= 23:
        print("Son las ", horas, ":", minutos, " de la noche", sep="")
    else:
        print("Son las ", horas, ":", minutos, " de la madrugada", sep="")
else:
    print("No es una hora válida")
