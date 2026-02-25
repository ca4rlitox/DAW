import random

print("Generando claves en el formato solicitado: ")
for i in range(0,100000000,1):
    print(random.randint(10000,100000),random.randint(10000,100000),random.randint(10000,100000),random.randint(10000,99999),random.randint(10000,100000),sep="-")

