entrada=False

while(entrada==False):
    num=input("Ingresar un numero entero: ")
    if num.isdigit():
        num=int(num)
        if num>0:
            entrada=True

suma=0
for i in range(1, num):
    if num%i==0:
        suma+=i

if suma==num:
    print("El número es perfecto")
else:
    print("El número no es perfecto")


