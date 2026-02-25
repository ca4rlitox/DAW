"""Un número abundante o número excesivo es un número para el cual la suma de sus divisores
propios es mayor que el propio número. El entero 12 es el primer número abundante. Sus
divisores propios son 1, 2, 3, 4 y 6 para un total de 16. La cantidad en que la suma excede al
número es la abundancia. El número 12 tiene una abundancia de 4, por ejemplo.
Los primeros 28 números abundantes son: 12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66,
70, 72, 78, 80, 84, 88, 90, 96, 100, 102, 104, 108 , 112, 114 y 120
Escribe una función que reciba dos números y nos muestre por consola todos los números
excesivos que hay entre ellos, ambos incluidos"""

num1=int(input("Ingresa un número: "))
num2=int(input("Ingresa otro número: "))

numUno=min(num1,num2)
numDos=max(num1,num2)

def compruebaNumAbundante(num):
    suma=0
    for i in range(1,num):
        if num%i==0:
            suma+=i
    if suma>num:
        return True

def identificaNumeros(num1, num2):
    for i in range(num1,num2+1):
        if compruebaNumAbundante(i):
            print(i,"es un número abundante")


identificaNumeros(numUno,numDos)