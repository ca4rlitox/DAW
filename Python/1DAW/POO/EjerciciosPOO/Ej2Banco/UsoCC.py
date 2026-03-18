from Banco import Banco
from CuentaCorriente import  CuentaCorriente
from Clientes import Clientes

banco1 = Banco("Lopez de Hoyos","Madrid","2100")
cliente1 = Clientes("Carlos", "Martín Codina", "58410447F","648573853",banco1.verSucursal)
cc1 = CuentaCorriente(cliente1,banco1)

cc1.verDatos(cliente1)
