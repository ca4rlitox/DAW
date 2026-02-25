"""Desarrolla una función que reciba como argumento un número en binario
(como una cadena de texto o String) y devuelva su valor en decimal.
A continuación tienes unos ejemplos de ejecución y la salida que producen en consola
print(toDecimal(“10110”))
print(toDecimal(“345”))
print(toDecimal(“hola”))
Salida en consola:
22
-1
-1
La funcíón debe de ser exactamente como se describe: el número en binario se recibe como
argumento y como string. El valor en decimal se devuelve (y no se imprime desde dentro
de la función). Si lo que se recibe no es un número en binario,
la función debe de devolver el valor -1
"""

numBinario=input("Ingrese un número binario")

def toDecimal(num):
    suma=0
    pos=0
    #if not compruebaNum(numBinario):
       # return -1
    numAlReves=num[-1::-1]
    #lista=list(numAlReves)
    for nume in numAlReves:
        if nume!="1" and nume!="0":
            return -1
        if nume=="1":
            suma=suma+2**int(pos)
        pos += 1
    return suma

print(toDecimal(numBinario))

"""def compruebaNum(numBinario):
    listaNum=list(numBinario)
    for num in listaNum:
        if num!="1" and num!="0":
            return False
    return True


while not compruebaNum(numBinario):
    numBinario=input("Ingrese un número binario")

print("Numero correcto")"""