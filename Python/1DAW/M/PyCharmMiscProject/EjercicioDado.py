import random

dado=1
contador=0

"""
while dado!=6:
    dado = random.randint(1,6)
    print (dado)
    contador+=1

if contador == 1:
    print ("He tenido que tirar el dado", contador, "vez")
else:
    print ("He tenido que tirar eldado" ,contador, "veces")
"""

dado1= 0
dado2= 1
contador = 0

while dado1!=dado2:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    contador+=1
    print (dado1, "-", dado2)

if contador == 1:
    print ("He tenido que tirar el dado", contador, "vez")
else:
    print ("He tenido que tirar eldado" ,contador, "veces")

    
