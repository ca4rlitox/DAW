inventario = {
    "manzanas": 50,
    "naranjas": 30,
    "plátanos": 40
}

def reponer_producto(nombre,cantidad):
    if comprobar_producto(nombre):
        inventario[nombre]+=cantidad
    else:
        inventario[nombre]=cantidad


def vender_producto(nombre, cantidad):
    if comprobar_producto(nombre):
        if inventario[nombre] >= cantidad:
            inventario[nombre]-=cantidad
        else:
                print(f"Stock insuficiente. Solo quedan {inventario[nombre]} unidades de {nombre}")
    else:
        print(f"El producto {nombre} no existe en el inventario")

def comprobar_producto(nombre):
    return nombre in inventario
    """for fruta, unidades in inventario.items():
        if fruta == nombre:
            return True
    return False"""


def mostrar_inventario():
    print("Inventario actual:")
    for fruta,cantidad in inventario.items():
        print(f"- {fruta}: {cantidad} unidades")


vender_producto("manzanas", 10)
vender_producto("naranjas", 100)
reponer_producto("peras", 20)
mostrar_inventario()