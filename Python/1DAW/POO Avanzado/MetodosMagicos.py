# __init__ es un metodo mágico
class Cuenta():
    def __init__(self,saldo):
        self.__saldo = saldo

    # como el metodo toString de Java
    def __str__(self):
        return "Saldo de cuenta:"+str(self.__saldo) #str para convertir el saldo en string

    # redefinir metodo para sumar objetos
    def __add__(self,cuenta2):
        self.__saldo+= cuenta2.__saldo

    # redefinir metodo >
    def __gt__(self,cuenta):
        mayor = True
        if cuenta2.__saldo > self.__saldo:
            mayor = False
        return mayor

cuenta1= Cuenta(100)
cuenta2 = Cuenta(200)

print(cuenta1,cuenta2)

cuenta1 = cuenta1 + cuenta2 #esto para el metodo magico __add__

print(cuenta1)

# __len__ -> se puede referir al method especial (dunder method) en Python que define cómo se calcula la longitud de un objeto, devolviendo un entero
# __add__ -> añade
# __mul__ -> multiplica
# __eq__ -> equals
# __gt__ -> greater than