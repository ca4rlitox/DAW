from Clientes import Clientes
from Banco import Banco
import random

class CuentaCorriente:
    def __init__(self,cliente,banco):
        cuenta = "ES34 "+str(banco.cod)+" "
        for i in range(0,12):
            cc = str(random.randint(0,9))
            cuenta+=cc
        self.cliente = cliente
        self.cuentacorriente = cuenta

    def verDatos(self):
        print(self.cuentacorriente)