"""Escribir un programa que muestre por pantalla los 5 primeros números primos, sus
raíces cuadradas, sus cuadrados y sus cubos"""

sumaPrimos=0
suma=0
i=1
while sumaPrimos<5:
    for j in range (1,i+1):
        if i%j==0:
            suma+=1
    if suma==2:
        print(i," es primo")
        print(i, " al cuadrado es: ",i**2)
        print(i, " al cubo es: ",i**3)
        print("La raiz cuadrada de ",i, " es: ",i**0.5,)
        sumaPrimos+=1
    i+=1
    suma=0