P = 27.93
R = 102.81
F = 0.93


E = float(input("Introduce la cantidad en euros para convertirlo\n"))
moneda = float(E[:-1])
P = E * P
R = E * R
F = E * F

print("Elige que quieres convertir de euros a\n")
print("P para pesos cubanos")
print("R para rupias")
print("F para francos suizos")
print("X para ver todos los cambios\n")
opcion = input("Opcion: ")



match opcion:
    case "P" | "p":
        print(E,"euros equivalen a",round(P,4),"pesos cubanos")
    case "R" | "r":
        print(E,"euros equivalen a",R,"rupias")
    case "F" | "f":
        print(E,"euros equivalen a",F,"francos suizos")
    case "X" | "x":
        print(E, "euros equivalen a", P, "pesos cubanos,", R, "rupias", "o", F, "francos suizos\n")
    case _:
        print("Error, letra no reconocida.\n")
