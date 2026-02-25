"""Escribe un programa que pida dos números a y b y genere una lista con todos
los números primos que estén entre a y b inclusive"""

a=int(input("Ingrese un número: "))
b=int(input("Ingrese otro número: "))
aux=0
suma=0
i=0
if a>b:
    a,b= b,a

for a in range(a,b+1):
    for i in range(1,a+1):
        resultado=a%i
        if resultado==0:
            suma+=1
    if suma==2:
        print(i)
    suma=0