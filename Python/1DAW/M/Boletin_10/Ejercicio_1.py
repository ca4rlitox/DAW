"""Se denominan números amigos a dos números naturales diferentes relacionados de tal
manera que la suma de los divisores propios de cada uno es igual al otro número.
Un divisor propio de un número es un factor positivo de ese número que no sea el propio
número. Por ejemplo, los divisores propios de 6 son 1, 2 y 3, pero no 6.
El par más pequeño de números amigos es (220, 284), y son amigos porque los divisores
propios de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y 110, de los cuales la suma es 284; y los
divisores propios de 284 son 1, 2, 4, 71 y 142, de los cuales la suma es 220
Los primeros diez pares de números amigos son: (220, 284), (1184, 1210), (2620, 2924),
(5020, 5564), (6232, 6368), (10744, 10856), (12285, 14595), (17296, 18416), (63020,
76084) y (66928, 66992)
Escribe una función que reciba dos números y devuelva un valor booleano que nos diga si
son amgos o no"""

num1=int(input("Ingresa un número: "))
num2=int(input("Ingresa otro número: "))

def calculaDivisores(num):
    suma=0
    for i in range(1,num):
        if num%i==0:
            suma+=i

    return suma



def compruebaNumAmigo(suma1,suma2,num1,num2):
    if(suma1==num2 and suma2==num1):
        return True
    else:
        return False


suma1=calculaDivisores(num1)
suma2=calculaDivisores(num2)
if compruebaNumAmigo(suma1,suma2,num1,num2):
    print("Los números son amigos")
else:
    print("Los números no son amigos")