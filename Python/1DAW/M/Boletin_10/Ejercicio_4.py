"""Un número defectivo o número deficiente es un número para el que la suma de sus divisores
propios es menor que el propio número. Por ejemplo, los divisores propios de 8 son 1, 2 y 4, y
su suma es menor que 8, por lo que 8 es deficiente.
Los primeros números deficientes son 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 21,
22, 23, 25, 26, 27, 29, 31, 32 , 33, 34, 35, 37, 38, 39, 41, 43, 44, 45, 46, 47, 49 y 50
Escribe una función que reciba dos números y nos muestre por consola todos los números
deficientes que hay entre ellos, ambos incluidos"""

num1=int(input("Ingresa un número: "))
num2=int(input("Ingresa otro número: "))

numUno=min(num1,num2)
numDos=max(num1,num2)

def compruebaNumDeficiente(num):
    suma=0
    for i in range(1,num):
        if num%i==0:
            suma+=i
    if suma<num:
        return True

def identificaNumeros(num1, num2):
    for i in range(num1,num2+1):
        if compruebaNumDeficiente(i):
            print(i,"es un número deficiente")


identificaNumeros(numUno,numDos)