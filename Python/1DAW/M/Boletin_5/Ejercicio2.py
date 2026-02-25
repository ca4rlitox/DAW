"""Hacer un programa en que nos permita calcular todos los divisores comunes a dos
números"""

num1=int(input("Introduce un numero: "))
num2=int(input("Introduce otro numero: "))

for i in range(1,num1+1):
    if num1 % i == 0 and num2 % i == 0:
        print(i ," es divisor de ",num1," y de ", num2)