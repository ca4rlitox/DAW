"""
2. En matemáticas, la sucesión de Fibonacci se trata de una serie infinita de números
naturales. Los dos primeros son siempre el 0 y el 1. Los siguientes se obtienen
sumando los dos anteriores. El tercero sería 1 (la suma de 0 + 1), el cuarto sería 2 (la
suma de 1 + 1), el quinto 3 (la suma de 1 + 2) y así sucesivamente. La lista con los 10
primeros números sería esta: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34].
Queremos hacer un programa que reciba un número por teclado y nos calcule tantos
números de la sucesión de fibonacci como indique ese número. Por ejemplo, si
metemos un 8 la salida de tu programa debería de ser así:
0,1,1,2,3,5,8,13
"""

num=int(input("Ingrese el número de sucesiones de fibonacci que desea conocer "))

a=0
print(a, end=",")
b=1
print(b,end=",")
for i in range(1,num-1):
    c=a+b
    if(i<num-2):
        print(c,end=",")
    else:
        print(c,end="")
    a=b
    b=c