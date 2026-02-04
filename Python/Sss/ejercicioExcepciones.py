sueldoCorrecto = False
while sueldoCorrecto == False:
    print("Inicio del programa")
    entrada = input("Ingrese el sueldo: ")
    try:
        sueldo = float(entrada)
    except:
        print("El sueldo no es valido")
    else:
        sueldoCorrecto=True