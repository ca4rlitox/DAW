""" Queremos ahora cambiar el sistema de codificación. Con el mismo pin (6240)
la salida ahora sería esta:
XXXXOOOOOO
XXXXXXXXOO
XXXXXXOOOO
XXXXXXXXXX
Escribe la función que lo realice. Ten en cuenta las mismas consideraciones que en
el ejercicio anterior"""

pin=int(input("Introduce tu pin (máximo 4 dígitos): "))
while len(str(pin)) > 4:
    pin=int(input("Introduce tu pin (máximo 4 dígitos): "))

lista=[]
def cifrarlinea(num):
    fila = ""
    for i in range(1,11):
        if i<=10-int(num):
            fila+="X"
        else:
            fila+="0"
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