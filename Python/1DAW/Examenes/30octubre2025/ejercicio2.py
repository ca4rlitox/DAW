cambioPesos = 27.93
cambioRupias = 102.81
cambioFrancos = 0.93

cantidad = input("Introduce la cantidad a convertir, seguido de la letra")
divisa = cantidad[-1]
cantidad = float(cantidad[:-1])

match divisa:
    case "E" | "e":         #con la barra vertical | podemos poner otras opciones para el case, por ejemplo que acepte mayuscula y minuscula
        print(f"{cantidad} euros equivalen a",round(cambioPesos*cantidad,4),"pesos cubanos, ",round(cambioRupias*cantidad,4),"rupias o",round(cambioFrancos*cantidad,4),"francos suizos")
    case "R" | "r":
        print(cantidad,"rupias equivalen a",round(cantidad/cambioRupias,4),"euros")
    case "F" | "f":
        print(cantidad,"francos suizos equivalen a",round(cantidad/cambioFrancos,4),"euros")
    case "P" | "p":
        print(cantidad,"pesos cubanos equivalen a",round(cantidad/cambioPesos,4),"euros")
    case "X" | "x":
        print("Has elegido salir")
    case _:     #default
        print("No has pulsado una opcion válida")

print("Fin del menú")