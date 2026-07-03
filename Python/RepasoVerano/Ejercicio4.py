# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

numero = int(input("Ingrese un numero: "))

for i in range(0,numero+1):
    if numero != i:
        print(numero-i,end=", ")
    elif numero-i == 0:
        print(numero-i,end="")