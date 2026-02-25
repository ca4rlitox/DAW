"""1. Escribir un programa donde se muestren los 10 primeros números enteros

2. Escribir un programa donde se muestren los 50 primeros números pares

3. Escribir un programa donde se muestren los 5 primeros números múltiplos de uno dado por
el usuario (se introducirá por teclado)

4. Escribir un programa donde se muestren todos los números divisibles por 7 menores a
10000

5. Escribir un programa que pida por teclado un número al usuario y diga si es par o impar"""

# 1

"""for i in range (1,10):
    print (i)
print ("FIN")"""

#2

"""for i in range (0,51,2):
    print (i)
print ("FIN")"""

#3

num = int(input("Introduce un numero para conocer sus 5 primeros multiplos "))

i=1
resultado=0
for i in range (i,6,1):
    print(resultado)
    resultado=num*i


"""while (num<1):
    print("El numero tiene que ser mayor que 1")
    num = int(input("Vuelve a introducir un numero "))
i = num
j=0
while(j<5 and i>=1):
    if(num%i==0):
        print(i)
        j+=1
    i-=1
if (j==4 or j==3 or j==2 or j==1 or j==0):
    print(num," no tiene mas multiplos")"""



#4
"""
i=10000
for i in range(i,1,-1):
    resultado = i % 7

    if resultado==0 :
        print(i)
"""

#5
"""num = int(input("Introduce un numero"))

if (num%2==0):
    print (num, "es par")
else:
    print (num, "no es par")"""
