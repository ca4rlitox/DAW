opcion = input("Escribe P para jugar, C para configurar, X para salir: ")

#sustituye al if cuando tenemos que comparar varias opciones

match opcion:
    case "P" | "p":         #con la barra vertical | podemos poner otras opciones para el case, por ejemplo que acepte mayuscula y minuscula
        print("Has elegido jugar")
    case "C" | "c":
        print("Has elegido configurar")
    case "X" | "x":
        print("Has elegido salir")
    case _:                             #averiguar que hace la barra baja _ ??????????????????????????
        print("No has pulsado una opcion válida")

print("Fin del menú")