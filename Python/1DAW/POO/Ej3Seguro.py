import datetime
from abc import ABC,abstractmethod

class Vehiculo(ABC):
    def __init__(self,conductor,matricula,ano_venta):
        self.conductor = conductor
        self.matricula = matricula
        self.ano_venta = ano_venta
    @abstractmethod
    def calcular_precio_seguro(self):
        pass

class Conductor:
    def __init__(self,nombre,nif,ano_nacimiento,ano_carnet,puntos_carnet):
        self.__nombre = nombre
        self.__nif = nif
        self.__ano_nacimiento = ano_nacimiento
        self.__ano_carnet = ano_carnet
        self.__puntos_carnet = puntos_carnet
    @property
    def getNombre(self):
        return self.__nombre
    @property
    def getAnoNacimiento(self):
        return int(self.__ano_nacimiento)
    @property
    def getAnoCarnet(self):
        return self.__ano_carnet
    @property
    def getPuntos(self):
        return self.__puntos_carnet

class Moto(Vehiculo):
    def __init__(self,conductor,matricula,ano_venta):
        super().__init__(conductor,matricula,ano_venta)

    def calcular_precio_seguro(self):
        anosCarnet = int(datetime.date.today().year) -self.conductor.getAnoCarnet
        anos = int(datetime.date.today().year) - self.conductor.getAnoNacimiento
        print(f"Vehículo: Moto. Matrícula: {self.matricula} Año de compra: {self.ano_venta}\n"
              f"Conductor: {self.conductor.getNombre}. Edad: {anos}. Años de carnet: {anosCarnet}. "
              f"Puntos: {self.conductor.getPuntos}")
        sumaTotal = 200
        if self.conductor.getPuntos < 8:
            sumaTotal+=150
        if anos < 24:
            sumaTotal+=25
        if anosCarnet < 2:
            sumaTotal+=50
        print(f"Precio del seguro a todo riesgo: {sumaTotal}€")
        print("No se hacen seguros a todo riesgo a motos")

        # 200€ anuales sumados a:
        # 150€ mas si el conductor tiene menos de 8 puntos
        # 25€ mas si el conductor tiene menos de 24 años
        # 50€ mas si el conductor tiene menos de dos años de carnet
        # No se hacen seguros a full riesgo de motos.

class Coche(Vehiculo):
    def __init__(self,conductor,matricula,ano_venta):
        super().__init__(conductor, matricula, ano_venta)

    def calcular_precio_seguro(self):
        anosCarnet = int(datetime.date.today().year) - self.conductor.getAnoCarnet
        anos = int(datetime.date.today().year) - self.conductor.getAnoNacimiento
        anosCoche = int(datetime.date.today().year) - self.ano_venta
        print(f"Vehículo: Moto. Matrícula: {self.matricula} Año de compra: {self.ano_venta}\n"
              f"Conductor: {self.conductor.getNombre}. Edad: {anos}. Años de carnet: {anosCarnet}. "
              f"Puntos: {self.conductor.getPuntos}")
        sumaTotalFull=0

        if anosCoche == 0 or anosCoche == 1:
            sumaTotalFull+=400
        if anosCoche == 2:
            sumaTotalFull+=500
        if anosCoche == 3:
            sumaTotalFull += 700
        if anosCoche >= 4:
            totalAnos=anosCoche*250
            sumaTotalFull+=totalAnos
        if self.conductor.getPuntos < 8:
            sumaTotalFull+=100

        print(f"Precio del seguro a todo riesgo: {sumaTotalFull}€")

        sumaTerceros = 250
        if self.conductor.getPuntos < 8:
            sumaTerceros += 100
        if anos < 24:
            sumaTerceros+=50
        if anosCarnet < 2:
            sumaTerceros+=75
        print(f"Precio del seguro a teceros: {sumaTerceros}€")


conductor1 = Conductor("Carlos","754758h", 2004, 2022, 8)
coche1 = Moto(conductor1,"6097GRZ",2021)

coche1.calcular_precio_seguro()