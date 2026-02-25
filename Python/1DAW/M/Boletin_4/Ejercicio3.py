"""
3. Queremos ahora hacer un programa que reciba un número por teclado y nos muestre en
orden todos los números de la sucesión de fibonacci que sean menores o iguales al que
has enviado como argumento. Por ejemplo, si metemos el número 4 nos debería de
devolver esto:
0,1,1,2,3
"""
num=int(input("Ingrese un número y se mostraran"
              "las sucesiones de fibonacci menores (o igual) a su número "))

a=0
print(a, end=",")
b=1
print(b,end=",")
c=0
while c<num-1:
    c=a+b
    a=b
    b=c
    if(c<num-1):
        print(c,end=",")
    else:
        print(c,end="")
        c=num
    c=a+b

