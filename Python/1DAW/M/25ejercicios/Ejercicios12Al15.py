"""12. Escribir un programa que sirva como asistente para un juego de rol. Tu programa debería de
pedir por teclado el número de dados que se van a tirar y el número de caras de estos (4, 6,
8, 12, etc.) A continuación debería de hacer la tirada y mostrarla.

13. Modifica el programa anterior para que no admita dados con un número de caras impares
(¡no existen!). En el caso de meter un número impar de caras el programa debería de
informarnos de que es erróneo y volver a preguntarnos por este dato.

14. Escribir un programa que nos pida dos números por teclado y genere un número aleatorio
comprendido entre ambos. Por el momento no te preocupes de que el primer número
siempre debería de ser menor que el segundo, simplemente no los metas en un orden
incorrecto.

15. Modificar el programa del punto anterior para que si el primer número que metemos es
mayor que el segundo funcione correctamente. Es decir, si metemos en primer lugar el 50 y
en segundo el 10 nos debería de generar un número aleatorio entre el 10 y el 50 (y no entre el
50 y el 10 que no tiene mucha lógica…)"""

import random


#12
"""numDados=int(input("Ingrese numero de dados "))
numCaras=int(input("Ingrese numero de caras "))


i=1
while (i<=numDados):
    dado = random.randint(1, numCaras)
    print(dado)
    i+=1
i=0
for i in range(i,numDados):
    dado = random.randint(1, numCaras)
    print(dado)"""

#13
"""numDados=int(input("Ingrese numero de dados "))
numCaras=int(input("Ingrese numero de caras "))
i=0
while(numCaras%2!=0):
    numCaras = int(input("el numero de caras no puede ser impar, ingrese denuevo "))

for i in range(i,numDados):
    dado = random.randint(1, numCaras)
    print(dado)"""

#14
"""num1 = int(input("Ingrese numero 1"))
num2 = int(input("Ingrese numero 2"))


numAleatorio= random.randint(num1, num2)
print(numAleatorio)"""

#15
num1 = int(input("Ingrese numero 1 "))
num2 = int(input("Ingrese numero 2 "))

if num1>num2:
    numAleatorio= random.randint(num2, num1)
    print(numAleatorio)
else:
    numAleatorio2= random.randint(num1, num2)
    print(numAleatorio2)

