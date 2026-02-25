"""Solicita una nota entre el 1 y el 10 (sin decimales) y devuelve
la calificación según la siguiente escala: 1-2 Muy deficiente, 3-4 Insuficiente,
5 Suficiente, 6 Bien, 7-8 Notable, 9-10 Sobresaliente"""

nota=int(input("Ingrese una nota (del 1 al 10) "))

match nota:
    case 1|2:
        print("Muy deficiente")
    case 3|4:
        print("Insuficiente")
    case 5:
        print("Suficiente")
    case 6:
        print("Bien")
    case 7|8:
        print("Notable")
    case 9| 10:
        print("Sobresaliente")
    case _:
        print("Nota fuera de rango")