class Sucursal:
    __banco = "ES68 1234"
    def __init__(self,direccion,provincia,codigo_id):
        self.__direccion = direccion
        self.__provincia = provincia
        self.__codigo_id = str(codigo_id)

class CuentaCorriente:
    def __init__(self,cod_id,saldo,titular1,titular2=None):
        self.__cod_id = cod_id
        self.__saldo = saldo
        self.titular = titular1
        titular1.cuentas.append(self)
        if titular2 is not None:
            self.__titular2 = titular2
            titular2.cuentas.append(self)
        @property
        def codigo(self):
            return self.__cod_id

class Cliente:
    def __init__(self,nombre,apellidos,nif,telefono,sucursal):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__nif = nif
        self.__telefono = telefono
        self.__sucursal = sucursal
        self.__cuentas = []

    @property
    def cuentas(self):
            return self.__cuentas

    def verCuentas(self):
        print(f"{self.__nombre} {self.__apellidos}. Cliente de la sucursal {self.__sucursal}")
        for cuenta in self.__cuentas:
            print(self.cuentas.codigo)



sucursal1 = Sucursal("calle del pez","madrid","0012")
cliente1 = Cliente("Pepe","Navarro","5548744R","644154805","0012")
cliente2 = Cliente("Maria","Navarro","5547744R","641047852","0012")
cc1 = CuentaCorriente("0012","453",cliente1,cliente2)

cliente1.verCuentas()