"""Desarrolla una función que reciba como argumento un número en decimal positivo y menor o
igual a 255 y devuelva su valor en binario como un octeto completo. A continuación tienes unos
ejemplos de ejecución y la salida que producen en consola
print(toBinario(22))
print(toBinario(129))
print(toBinario(345))
print(toBinario(22.5))
print(toBinario(“hola”))
print(toBinario(-2))
Salida en consola:
00010110
10000001
-1
-1
-1
-1
La funcíón debe de ser exactamente como se describe: el número en decimal se recibe como
argumento. El valor en binario se devuelve (y no se imprime desde dentro de la función) como String
(si no los ceros a la izquierda desaparecerían) y como un octeto completo. Si lo que se recibe no es
válido (un string, un número decimal, negativo o superior a 255) tu función devolverá un -1"""

numDecimal=input("Ingresa un número positivo menor o igual a 255: ")

def toBinario(numDecimal):
    if not compruebaNum(numDecimal):
        return -1
    else:
        pos=128
        numBinario=""
        i=0
        numEntero=int(numDecimal)
        while i<8:
            if numEntero>=pos:
                numEntero=numEntero-pos
                numBinario+="1"
                pos=pos//2
            elif numEntero<pos:
                pos=pos//2
                numBinario+="0"
            i+=1
        return numBinario

def compruebaNum(num):
    for n in num:
        if not num.isdigit():
            return False
    #numEntero=int(num)
    if 0<int(num)>255:
        return False
    return True

print(toBinario(numDecimal))