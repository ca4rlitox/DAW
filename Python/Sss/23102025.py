opcion = input("Escribe P para jugar, C para configurar, X para salir\n")

match opcion:
    case "P" | "p":
        print("Has elegido jugar\n")
    case "C" | "c":
        print("Has elegido configurar\n")
    case "X" | "x":
        print("Has elegido salir :-(\n")
    case _:
        print("Primo que has puesto? Elige bien \n")


print("...Fin del menu...")