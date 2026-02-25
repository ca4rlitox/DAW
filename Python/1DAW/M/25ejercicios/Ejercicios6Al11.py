#6. Escribir un programa que pida por teclado un número al usuario y diga si es divisible por 3 o
#no.

#7. Escribir un programa que pida un número por teclado al usuario que simule ser el precio de
#un artículo y escriba el resultado de aplicarle el IVA del 21%

#8. Escribir un programa que reciba por teclado el importe de una cantidad a pagar en euros
#(puede tener decimales) y el número de meses que contamos para pagarla (tiene que ser un
#número entero) y nos devuelva el dinero que tendríamos que pagar cada mes. No aplicamos
#intereses de ningún tipo y redondeamos a dos decimales.

#9. Escribir un programa que genere un número aleatorio entre el 0 y el 50 y lo muestre

#10. Escribir un programa que genere dos números aleatorios simultáneamente entre el 1 y el 6
#(simulando una tirada de dos dados)

#11. Modificar el programa anterior para que tu programa tire dos dados de forma continuada
#hasta que el número que salga en ambos sea el mismo. En ese momento debería de parar la
#ejecución e informarnos de cuantas tiradas ha tenido que hacer para llegar a ese resultado

import random

#6
"""
num=int(input("ingrese un numero"))

if (num%3==0):
    print(num, "es divisible por 3")
else:
    print(num, "no es divisible por 3")
    """

#7
precio=float(input("ingrese el precio para aplicar el iva"))

precioIva= round(precio*1.21,2) #usamos round() para redondear, espera recibir dos valores: el numero que quiere redondear (multiplicacion) y los decimales

print("el precio con iva es", precioIva)


#8
"""
importe=float(input("Ingrese el precio"))
meses=int(input("ingrese el numero de meses"))
cuota=importe/meses
print("la cuota total a pagar por mes es ",round(cuota,2), "Euros")
"""

#9
"""numAleatorio = random.randint(1,50)
print(numAleatorio)"""

#10
"""dado1=random.randint(1,6)
dado2=random.randint(1,6)
print(dado1,dado2)"""

#11

"""while dado1!=dado2:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print(dado1,dado2)"""






