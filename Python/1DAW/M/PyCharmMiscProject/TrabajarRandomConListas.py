import random

lista=["Manuel", "pepe", "Luis", "Maria"]

print(random.choice(lista))#elijo un elemento al azar de la lista
print(random.sample(lista,3))#elijo 3  elemntos al azar de la lista sin repetir
random.shuffle(lista)#reordena la lista al azar
print(lista)

