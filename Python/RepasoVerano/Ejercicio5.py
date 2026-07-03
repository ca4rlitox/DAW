# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y
# muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

cantidad = float(input("Introduce la cantidad a invertir: "))
interes = int(input("Introduce el interes anual: "))
anos = int(input("Introduce el numero de años: "))

interes = interes / 100

for i in range(1,anos+1):
    ganacia = cantidad * interes
    cantidad+=ganacia
    print("Año:",i,"cantidad: ",cantidad)