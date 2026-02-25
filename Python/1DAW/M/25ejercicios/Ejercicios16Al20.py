"""
16. Escribir un programa que genere seis números aleatorios entre el 1 y el 49 (simulando una
lotería primitiva). Por el momento no te preocupes de que algunos números puedan salir
repetidos. Ya resolveremos eso más adelante.

17. Escribir un programa que nos permita generar una quiniela. Para ello nos debe generar
quince números aleatorios entre el 1 y el 3. Recuerda que los resultados válidos son 1 X o 2,
así que si te sale un 3 lo que tienes que imprimir en pantalla es una X

18. Escribe un programa que genere números aleatorios entre el 1 y el 1000 sin parar y que sólo
se detenga cuando salga el 666. Los números que ha tenido que generar tu programa hasta
aparecer el 666 son los que restan para el apocalipsis. Tu programa debería de indicarlo con
un mensaje tétrico (¡Faltan 236 días para que se acabe todo! por ejemplo)

19. Escribir un programa que pida un número por teclado y nos muestre sus divisores

20. Escribir un programa que nos pida tres números por teclado en cualquier orden y nos los
muestre en pantalla ordenados de menor a mayor
"""

import random

#16
i=0
for i in range (i,6):
    numRandom = random.randint(1, 49)
    print (numRandom)

#17
i=0
for i in range (i,15):
    numRandom = random.randint(1, 3)
    if (numRandom==3):
        numRandom = 'X'
    print (numRandom)

#18
num= random.randint(1,1000)
dias= 0
while (num!=666):
    dias=dias+num
    num = random.randint(1, 1000)

print ("Tienes ", dias," días para que alguien te ame antes de que acabe el mundo")

#19
"""num = int(input("Ingrese un número mayor que 0: "))
i=num
for i in range (i, 1, -1):
    if (num%i==0):
        print (i)"""

#20
num1= int(input("Ingrese el primer número "))
num2= int(input("Ingrese el segundo número "))
num3= int(input("ingrese el tercer número "))

"""if (num1>num2 and num2>num3):
    print (num1, ", ", num2, ", ", num3)
elif(num1>num3 and num3>num2):
    print(num1, ", ", num3, ", ", num2)
elif(num2>num3 and num3>num1):
    print (num2, ", ", num3, ", ", num1)
elif (num2>num1 and num1>num3):
    print(num2, ", ", num1, ", ", num3)
elif (num3>num2 and num2>num1):
    print(num3, ", ", num2, ", ", num1)
else:
    print(num3, ", ", num1, ", ", num2)"""




