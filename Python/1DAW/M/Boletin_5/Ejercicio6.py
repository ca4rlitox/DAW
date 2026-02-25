"""Escribe un programa que nos permita contar el número de veces que se
repite cada cifra en un número. Por ejemplo, el número 885210003 tiene
tres 0, un 1, un 2, un 5 y dos 8.
A continuación tienes un ejemplo de ejecución:
Introduce un número: 885210003
Tu número tiene:
2 números 8
1 número 5
1 número 3
1 número 2
3 números 0
Fíjate que en la salida no deben de aparecer las cifras que no tenga el número. También
que se distingue el caso en que sólo haya una aparición (la palabra número aparece en
singular en estos casos"""

num=input("Introduce un numero: ")
lista=[]
for i in range(0,len(num)):
    lista.append(num[i])
lista2=[]
for numero in lista:
    if numero not in lista2:
        lista2.append(numero)

print("Tu número tiene")
contadorNum=[]
for numero in lista2:
    contador=(lista.count(numero))
    if contador==1:
        print(contador," numero ",numero)
    else:
        print(contador," numeros ",numero)





