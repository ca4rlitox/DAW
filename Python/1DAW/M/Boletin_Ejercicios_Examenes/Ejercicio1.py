"""Queremos escribir un programa que nos permita esconder un número pin de cuatro cifras por un
método muy sencillo. Imagínate que tu pin es el 6240. La salida por consola sería así:
XXXXXOXXXX
XOXXXXXXXX
XXXOXXXXXX
XXXXXXXXXO
Escribe una función que reciba como argumento un pin numérico de 4 cifras (por ejemplo 6420) y
devuelva una estructura con cuatro elementos cada uno de los cuales es una línea. Luego,
muestra en consola el resultado tal y como se ve aquí arriba. La función debe de ser exactamente
como se describe: el pin se recibe como un argumento numérico. La función devuelve una
estructura (no la muestra) y hay que mostrarla como aquí arriba desde fuera de la función.
NOTAS: Fíjate que el 0 se corresponde con la última posición y no con la primera
Piensa que los primeros dígitos del pin pueden ser 0 (ejemplo: 125, 40 o 7) y que como el argumento
de la función que se pide es un entero no puedes escribir 0040, pero tu función debe de funcionar
también correctamente en estos casos
Se valorará si haces el desarrollo de forma modular usando una función que reciba un entero y
devuelva la línea correspondiente. Eso permitiría en un futuro modificar el método de cifrado
fácilmente"""

pin=int(input("Introduce tu pin (máximo 4 dígitos): "))
while len(str(pin)) > 4:
    pin=int(input("Introduce tu pin (máximo 4 dígitos): "))

lista=[]
def cifrarlinea(num):
    fila = ""
    for i in range(1,11):
        if i==int(num):
            fila+="0"
        elif i==10 and int(num)==0:
            fila+="0"
        else:
            fila+="X"
    lista.append(fila)
    return lista

def cifrarpin(pin):
    pinTexto=str(pin)
    while len(pinTexto)<4:
        pinTexto="0"+pinTexto
    for num in pinTexto:
        cifrarlinea(num)

cifrarpin(pin)

for fila in lista:
    print(fila)

