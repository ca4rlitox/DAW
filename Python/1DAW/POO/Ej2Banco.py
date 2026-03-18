class Sucursal:
    def __init__(self,direccion,provincia,cod_id):
        self.__direccion = direccion
        self.__provincia = provincia
        self.__cod_id = cod_id
        self.__cuentas = []
    @property
    def getCodSucursal(self):
        return self.__cod_id
    @property
    def getCuentasSucursal(self):
        saldoTotal = 0
        print(f"Cuentas de la sucursal {self.__cod_id} ({self.__provincia})")
        for i in self.__cuentas:
            print(f"{i.getCodCuenta} - Saldo: {round(i.getSaldo,2)}€")
            saldoTotal+=i.getSaldo
        print(f"Saldo total: {round(saldoTotal,2)}€")
    def agregarCuenta(self,cuenta):
        self.__cuentas.append(cuenta)

class Cliente:
    def __init__(self,nombre,apellidos,nif,telefono,sucursal):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__nif = nif
        self.__telefono = telefono
        self.__sucursal = sucursal
        self.__cuentas = []

    def agregarCuenta(self, cuenta):
        self.__cuentas.append(cuenta)
        self.__sucursal.agregarCuenta(cuenta)

class CuentaCorriente:
    __codCuenta = "ES68 1234 "
    def __init__(self,codCuenta,saldo,titular1,titular2=None):
        self.__codCuenta+= codCuenta
        self.__saldo = saldo
        self.__titular1 = titular1
        if titular2 is not None:
            self.titular2 = titular2
    @property
    def getSaldo(self):
        return self.__saldo

    @property
    def getCodCuenta(self):
        return self.__codCuenta

sucursal_madrid = Sucursal("Gran Vía 1", "Madrid", "2100")
cliente_juan = Cliente("Juan", "Pérez", "12345678A", "600123456", sucursal_madrid)

cuenta1 = CuentaCorriente("5555 6666", 1500, cliente_juan)
cuenta2 = CuentaCorriente("7777 8888", 3200, cliente_juan)

cliente_juan.agregarCuenta(cuenta1)
cliente_juan.agregarCuenta(cuenta2)

sucursal_madrid.getCuentasSucursal()