"""Escribe un programa que genere 100 números aleatorios comprendidos entre el 1 y 50
(ambos inclusive) y, posteriormente, obtenga el mayor, el menor y el que mas veces se
repite (y nos diga cuantas veces lo hace).
"""
import random

numAleatorios=[random.randint(1,50) for _ in range(0,100)]
"""
print("El número mayor es: ",max(numAleatorios))
print("El número menor es: ",min(numAleatorios))

contador=[0]*50 #array vacío con 50 posiciones
for i in range(1,51): #el número maximo que puede contener el array es 50 por lo tanto recorremos todos los números
    for numero in numAleatorios: #y por cada número de i, lo vamos a comparar con cada número del array
        if numero==i: #en los momentos que encuentre igualdad entre los números del array con el número de i
            contador[i-1]+=1 #si hay coincidencia lo guarda en la posicion del contador que equivale a i menos 1

#con index separo dentro del array la posicion mas alta, con mayores repeticiones
numeroMasRepetido=contador.index(max(contador))+1 #el número mas repetido se encuentra en el valor mayor del contador
print("El número que más se repite es: ",numeroMasRepetido, " y se repite ",max(contador), " veces")
"""
"""con index separo dentro del array la posición más alta, con mayores repeticiones.
numeroMasRepetido pasa a ser la posición del contador, pero al sumarle 1
y como el contador va de uno en uno (para la posición 0 el número que evalúa es el 1
para la posición 1 el número que evalúa es el 2) coincide con el número más repetido. 
Y lo que hace dentro (lo que almacena en la posición) es contar el número de
veces que se repite"""

#MIRARLO CON ESTE METODO

lista=[1,4,5,6,33,4,22,45,2,4,7]
mayor =-1
numeroMayor=0
for numero in lista:
    if lista.count(numero)>mayor:
        mayor= lista.count(numero)
        numeroMayor=numero

print("El mayor es",numeroMayor,"y se repite",mayor,"veces.")