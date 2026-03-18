from abc import ABCMeta, abstractmethod


class Persona(metaclass=ABCMeta):
    def __init__(self, nombre, apellidos, tlf):
        self.nombre=nombre
        self.apellidos = apellidos
        self.telefono = tlf
    @abstractmethod
    def verDatos(self):
        print(self.apellidos,"",self.nombre)


class Profesor(Persona):
    def __init__(self,nombre,apellidos,tlf):
        super().__init__(nombre,apellidos,tlf)
    def verDatos(self):
        print(self.apellidos,"",self.nombre)

class Alumno(Persona):
    def __init__(self,nombre,apellidos,tlf):
        print(self.apellidos,"",self.nombre)

