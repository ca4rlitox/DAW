from Clientes import Clientes
from Banco import Banco
import random

class CuentaCorriente:
    def __init__(self,cliente,banco):
        self.banco = banco
        cuenta = "ES34 "+self.banco.cod+" "
        for i in range(0,12):
            cc = str(random.randint(0,9))
            cuenta+=cc
        self.cliente = cliente
        self.cuentacorriente = cuenta

    def verDatos(self,cliente):
        print(f"{cliente.nombre} {cliente.apellidos}. Cliente de la sucursal {cliente.sucursal} ({cliente.provincia})")
        print(self.cuentacorriente)