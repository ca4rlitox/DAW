"""Modifica ahora tu programa para que, además, admita las horas en formato de 12 horas
poniendo am o pm después de la hora (6:55am o 11:30pm, por ejemplo). Si tu hora no
lleva ni am ni pm después se piensa que está en formato de 24 horas"""

hora = input("Introduce una hora en formato 24 horas (HH:MM) ")
dosPuntos = hora.index(':')
horas = hora[:dosPuntos]
minutos = hora[dosPuntos + 1:]


if 0 <= int(horas) <= 23 and 60 > int(minutos) >= 0:

    if int(horas)>12:
        horas=int(horas)-12
        print("Son las ",horas,":",minutos,"pm",sep="")
    elif 0<int(horas)<12:
        print("son las ",horas,":",minutos,"am",sep="")
    else:
        print("Son las 12:",minutos,"pm",sep="")
else:
    print("No es una hora válida")