"""Un número perfecto es un número entero positivo que es igual a la suma de sus divisores
propios positivos excluyéndose a sí mismo. Dicho de otra forma, un número perfecto es
aquel que es amigo de sí mismo.
Así, 6 es un número perfecto porque sus divisores propios positivos son 1, 2 y 3; y 6 = 1 + 2 +
3. Un divisor propio positivo de un número es un factor positivo de ese número que no sea el
propio número. Por ejemplo, los divisores propios de 6 son 1, 2 y 3, pero no 6. Los siguientes
números perfectos son 28, 496 y 8128.
Escribe una función que reciba un número y nos devuelva un valor booleano diciendo si es
perfecto o no. El número debe de recogerse por teclado y si no es un entero positivo se
debería de informar al usuario y pedir otro hasta que sea correcto. Usa excepciones para ello"""

num=int(input("Ingresa un número: "))

def compruebaNumPerfecto(num):
    suma=0
    for i in range(1,num):
        if(num%i==0):
            suma+=i

    if num==suma:
        return True

if compruebaNumPerfecto(num):
    print("El número",num,"es perfecto")
else:
    print(num,"no es un número perfecto")