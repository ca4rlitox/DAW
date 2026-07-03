# Escribir un programa que pida al usuario un número entero positivo y
# muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

numero = int(input("Ingrese un numero entero positivo: "))

if numero > 0:
    for i in range(1,numero+1):
        if i % 2 != 0 and i != numero:
            print(i,end=", ")
        elif i == numero:
            print(i,end="")
else:
    print("El número es negativo primo.")