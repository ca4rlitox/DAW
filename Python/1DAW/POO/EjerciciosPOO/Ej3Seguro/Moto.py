from POO.EjerciciosPOO.Ej3Seguro.Conductor import Conductor
from Vehiculo import Vehiculo
from datetime import date,datetime,time,timedelta

class Moto(Vehiculo):
    def __init__(self,conductor,matricula,ano_venta):
        super().__init__(conductor,matricula,ano_venta)
        hoy = date.today().year
        self.ano_venta = ano_venta
        self.cocheanos = self.ano_venta - int(hoy)
        self.anosCarnet = Conductor.verFechaNacimiento()

    def calcularSeguro(self,vehiculo,conductor,ano_venta):
        sumaseguro = 200
        if conductor.puntos < 8:
            sumaseguro+=150
        if self.edadConductor < 24:
            sumaseguro+=25
        if self.anosCarnet < 2:
            sumaseguro+=50
        print(f"Precio del seguro a terceros: {sumaseguro}€.\n"
            f"No se hacen seguros a todo riesgo a motos")


# 200€ anuales sumados a:
# 150€ mas si el conductor tiene menos de 8 puntos
# 25€ mas si el conductor tiene menos de 24 años
# 50€ mas si el conductor tiene menos de dos años de carnet
# No se hacen seguros a full riesgo de motos.