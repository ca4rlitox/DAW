""". Sabrás, por las clases de Sistemas de la Información, que, una IP de la versión 4 está formada por
cuatro bytes y que en relación a su primer byte podemos saber de que clase es y su máscara (si
estamos usando direccionamiento sin clases):
• En las clase A el primer byte tiene que estar entre el 0 y el 127, ambos inclusive y la máscara
es /8
• En las clase B el primer byte tiene que estar entre el 128 y el 191, ambos inclusive y la
máscara es /16
• En las clase C el primer byte tiene que estar entre el 192 y el 223, ambos inclusive y su
máscara es /24
• Entre el 224 y el 255, ambos inclusive, las direcciones se consideran reservadas (clases D y E)
• Por encima del 255 no son válidas
Escribe un programa que te pida una dirección IP sin máscara por el teclado y te la escriba en
consola poniéndole la máscara adecuada. Un ejemplo de ejecución podría ser así:
Introduce una dirección IP: 8.8.8.8
8.8.8.8/8
Si la dirección IP introducida es reservada o no válida tu programa debería de darte un mensaje por
pantalla :
Introduce una dirección IP: 230.0.0.0
Dirección reservada
Introduce una dirección IP: 300.1.1.1
Dirección no válida
Introduce una dirección IP: OLAKASE
Dirección no válida
NOTA: Tu programa debería de contemplar también, a la hora de decir que una IP no es válida, que
no tenga el formato adecuado (cuatro números enteros positivos separados por puntos y nunca
superiores al 255)"""

ip=input("Introduce una direccion IP: ")
lista=ip.split(".")

def devuelveIp(ip):
    if compruebaIp(ip):
        if int(lista[0]) < 128:
            print(ip,"/8",sep="")
        elif 127 < int(lista[0]) < 192:
            print(ip,"/16",sep="")
        elif 191 < int(lista[0]) < 224:
            print(ip,"/24",sep="")
        else:
            print("Direccion reservada")


def compruebaIp(ip):
    for i in ip:
        if not i.isdigit() and i != ".":
            return False
    if len(lista) != 4:
        return False
    for num in lista:
        if not num.isdigit():
            return False
        elif 0 > int(num) > 255:
            return False
    return True

while not compruebaIp(ip):
    ip=input("Dirección no válida\nIntroduce una direccion IP: ")

devuelveIp(ip)

