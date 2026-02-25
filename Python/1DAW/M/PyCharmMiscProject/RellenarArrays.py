import random


secuecencia = [i for i in range(2,50,2)] #genera una lista de pares del 2 al 49 // primero i para indicar que queremos meterlo en la lista
print(secuecencia)


secuencia = [random.randint(1,6) for _ in range(0,10)] #genera una lista de 10 posiciones de numeros random del 1 al 6
print(secuencia)

