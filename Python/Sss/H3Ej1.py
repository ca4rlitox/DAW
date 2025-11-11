# Escribir un programa que pida una contraseña por teclado (dos veces) y si no
# coinciden nos lo vuelva a pedir hasta que lo hagan

error=0

contra1 = input("Introduce la contraseña")
contra2 = input("Confirma la contraseña")

while contra1 != contra2:
    print("Error. Prueba otra vez")
    error = error + 1
    contra1 = input("Introduce la contraseña")
    contra2 = input("Confirma la contraseña")
else:
    print("Contraseña cambiada. Numero de fallos:",error)

# Modifica el programa anterior para que cuando coincidan ambas contraseñas nos informe del número de intentos inválidos