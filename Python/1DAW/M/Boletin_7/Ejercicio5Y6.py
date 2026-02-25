"""Pide al usuario un número y crea un array de enteros de tantas posiciones
como indique ese número. Rellenalo con números aleatorios entre el 10 y el 1000
y finalmente muestra cual es el máximo, cual el mínimo y la media aritmética
con dos decimales.
Modifica el ejercicio anterior para que, nos muestre en que posición del array se
encuentran el máximo y el mínimo. Si están repetidos y aparecen en mas de una
posición debería de indicarlas todas
"""
import random
num=int(input("Ingresa un número"))
suma=0
numeros=[random.randint(10,1000) for i in range(num)]

maximo=max(numeros)
print(f"El máximo de la lista es {maximo}")
print("Y se encuentra en la/s posicion/es",end=": ")
for i,numero in enumerate(numeros):
    if numero==maximo:
        print(i+1,end=",")

print()

minimo=min(numeros)
print(f"El mínimo de la lista es {minimo}")
print("Y se encuentra en la/s posicion/es:", end="")
for i, numero in enumerate(numeros):
    if numero==minimo:
        print(i+1, end=", ")

print()
for numero in numeros:
    suma+=numero

print(f"El promedio de los números de la lista es {round(suma/num,2)}")


