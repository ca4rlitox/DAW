
# Las clases se definen con la primera en mayúscula y en singular
class Alumno:
    # Constructor
    #self es como el this de java
    def __init__(self, nombre, edad, marica):
        self.__nombre = nombre
        self.__edad = edad
        self.__marica = marica

    ## Para ver datos
    def verDatos(self):
        print(f"Nombre: {self.__nombre} edad: {self.__edad} marica: {self.__marica}") # el ultimo atributo es uno protegido por el __
    ## Para ver datos o establecerlos (metodo java)
    # def setEdad(self,ed): #Como en Java el setter
    #    self.__edad = ed
    # def getEdad(self):
    #    return self.__edad
    #metodo de python
    @property #para un getter se pone esto
    def edad(self):
        return self.__edad
    @edad.setter #para un setter
    def edad(self,ed):
        self.__edad = ed

trista=Alumno("Leandro Trista", 33, "no")
carlos=Alumno("Carlos Martin",21,"si")

trista.edad = 55

print(trista.edad)
#public: edad
#protected: _edad (dentro de la clase)
#private: __private (dentro de la clase)
print(carlos.edad)
