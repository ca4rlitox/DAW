from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self,conductor,matricula,ano_venta):
        self.conductor = conductor
        self.matricula = matricula
        self.ano_venta = ano_venta
    @abstractmethod
    def calcularSeguro(self,vehiculo,persona,ano_venta):
        pass