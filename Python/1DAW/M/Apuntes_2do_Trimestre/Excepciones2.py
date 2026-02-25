print("Inicio del programa")
esCorrecto=False
"""while not esCorrecto:
    try:
        entrada = input("Introduce tu sueldo")
        sueldo= float(entrada)
        #esCorrecto=True puedo ponerlo aca pero para que sea mas ordenado puedo ponerlo en un else
    except ValueError:
        print("Sueldo ingresado no valido, vuelve a ingresar")
        esCorrecto=False
    else:
        esCorrecto=True

print(sueldo)"""

while True:
    try: #aqui van las instrucciones que son sensibles a provocar un error
        entrada=input("Introduce tu sueldo")
        sueldo=float(entrada)
        break
    except ValueError: #aqui se pone lo que se hace en caso de que sea un error
        print("Sueldo ingresado no valido, vuelve a ingresar")

print(sueldo)

