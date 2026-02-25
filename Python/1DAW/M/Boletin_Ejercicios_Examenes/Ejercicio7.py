"""7. Escribe una función que reciba un como argumento un número variable de strings y nos diga,
por cada uno de ellos si se trata de una dirección MAC válida o no. Las direcciones MAC, por si no lo
recuerdas de las clases de sistemas de información, están formadas por seis bytes expresados en
hexadecimal. Por ejemplo así:
F4:8E:38:AF:F4:1C
Cada cifra en hexadecimal no puede ser mayor que 255, es decir, de FF. Tú función debe de
contemplar que las letras correspondientes a las cifras A-F del hexadecimal pueden venir en
mayúsculas o en minúsculas y debería de darlas como válidas en ambos casos. También que a
veces se escribe separando cada byte de forma independiente con dos puntos (como en el ejemplo
anterior) o en el formato que usa CISCO, separando cada dos bytes con un punto. Así:
F48E.38AF.F41C
A continuación dos ejemplos de llamada a la función con sus respectivas salidas en consola:
macsValidas(“F4:8E:38:AF:F4:1C”, “7521-MXP”)
F4:8E:38:AF:F4:1C es válida
7521-MXP no es válida
MACs válidas: 1
MACs no válidas: 1
macsValidas(“F48E38AFF41C”,“f48e.38af.f41c”,“F:3:AF:4:1:11”)
F48E38AFF41C no es válida
f48e.38af.f41c es válida
F:3:AF:4:1:11 no es válida
MACs válidas: 1
MACs no válidas: 2
NOTA: Se valorará si haces el desarrollo de forma modular usando una función que reciba una MAC
y devuelva un valor booleano diciendo si es válida o no."""
opcion=input("Ingresa 1 para introducir direccion\nIngresa cualquier otra tecla para terminar\n")
validas = 0
noValidas = 0


def macsValidas(dirMAC):
    if dirMAC.find(".") != -1:
        lista = dirMAC.split(".")
        if len(lista) != 3:
            return False
        for pos in lista:
            if len(pos) != 4:
                return False
            for i in pos:
                if not i.isalnum():
                    return False
                if i > "F":
                    return False
    elif dirMAC.find(":") != -1:
        lista = dirMAC.split(":")
        if len(lista) != 6:
            return False
        for pos in lista:
            if len(pos) != 2:
                return False
            for i in pos:
                if not i.isalnum():
                    return False
                if i > "F":
                    return False
    else:
        return False
    return True
while opcion == "1":
    dirMAC=input("Introduce una direccion MAC: ").upper()
    if macsValidas(dirMAC):
        print(dirMAC,"es válida")
        validas+=1
    else:
        print(dirMAC,"no es válida")
        noValidas+=1
    opcion = input("Ingresa 1 para introducir direccion\nIngresa cualquier otra tecla para terminar\n")

print("MACs válidas: ",validas)
print("MACs no válidas: ",noValidas)