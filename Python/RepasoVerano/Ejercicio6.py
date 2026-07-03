# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo
# como el de más abajo, de altura el número introducido.

altura = int(input("Introduce un número entero: "))
contador = 1
for i in range(0,altura):
    for j in range(0,contador):
        print("*",end="")
    contador += 1
    print("\n",end="")