"""Hacer un programa que lea un número y un carácter y visualice una matriz compacta
repitiendo ese carácter y con tantas filas y columnas como indique el número. Por
ejemplo, si metemos el 4 y la x nos debería de mostrar esto:
xxxx
xxxx
xxxx
xxxx"""

num=int(input("Introduce un número: "))
caracter=input("Introduce un carácter: ")
for i in range(1,num+1):
    for j in range(1,num+1):
        print (caracter, end="")
    print()


