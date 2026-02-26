import random

for i in range(0,5):
    if i > 0:
        print("-",end="")
    for j in range (0,5):
        numeroRandom = random.randint(0,9)
        print(numeroRandom,end="")