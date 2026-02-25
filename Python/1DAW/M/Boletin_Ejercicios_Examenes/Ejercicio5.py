"""Escribe una función que reciba dos números enteros, positivos y mayores
a cero y te calcule los divisores comunes que tienen ambos.
A continuación tienes unos ejemplos de ejecución y la salida que producen en consola
divisoresComunes(22, 16)
divisoresComunes(33, 17)
divisoresComunes(1725, 2500)
Salida en consola:
Los divisores comunes de 22 y 16 son: 1, 2
El único divisor común de 33 y 17 es: 1
Los divisores comunes de 1725 y 2500 son: 1, 5, 25
Si alguno de los argumentos no cumple con lo dicho aquí arriba,
tu función debería de mostrar un mensaje de error:
divisoresComunes(22.5, 0)
No puedo calcular los divisores comunes de esos números
NOTAS: Se valorará si haces el desarrollo de forma modular usando una función
que reciba un número y devuelva todos sus divisores en el formato que creas oportuno.
Fíjate que tu función debería de distinguir en la salida el caso en que el divisor
común es únicamente el 1
Los divisores comunes deberían de mostrarse ordenados de forma ascendente"""

num1=input("Ingresa un número mayor a 0: ")
num2=input("Ingresa otro número mayor a 0: ")
lista = []

def devuelveNumeros():
    if len(lista)==1:
        print("El único divisor común de 33 y 17 es: ",lista[0])
    else:
        print("Los divisores comunes de ",num1,"y",num2," son: ",end="")
        cont=0
        for num in lista:
            if cont == len(lista)-1:
                print(num)
            else:
                print(num,end=", ")
            cont+=1

def divisoresComunes(num1, num2):
    if not compruebaNumero(num1, num2):
        print("-1")
    else:
        menor=min(int(num1),int(num2))
        mayor=max(int(num1),int(num2))
        cont=0
        for i in range (1,menor+1):
            if menor%i==0 and mayor%i==0:
                lista.append(i)
        devuelveNumeros()


def compruebaNumero(num1,num2):
    num=num1+num2
    for n in num:
        if not n.isdigit():
            return False
    if int(num1)<1 or int(num2)<1:
        return False
    return True

divisoresComunes(num1, num2)

