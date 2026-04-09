from abc import ABCMeta, abstractmethod

class Persona(metaclass=ABCMeta):
    def __init__(self, nombre):
        self.__nombre=nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom

    @abstractmethod
    def __str__(self):
        pass

    @staticmethod
    def verLista(personajes):
        for personaje in personajes:
            print(personaje)

class Futbolista(Persona):
    def __init__(self,nombre, altura, equipo, edad, dorsal):
        super().__init__(nombre)
        self.__altura=altura
        self.__equipo=equipo
        self.__edad=edad
        self.__dorsal=dorsal

    def __str__(self):
        return f"\nNombre: {self.__nombre}\nAltura: {self.__altura}\nEquipo: {self.__equipo}\nEdad: {self.__edad}\nDorsal habitual: {self.__dorsal}"

class Anime(Persona):
    def __init__(self,nombre,anime,mangaka):
        super().__init__(nombre)
        self.__anime=anime
        self.__mangaka=mangaka

    def __str__(self):
        return f"\nNombre: {self.__nombre}\nAnime: {self.__anime}\nMangaka: {self.__mangaka}"

class Superheroe(Persona):
    def __init__(self,nombre, superheroe, editorial):
        super().__init__(nombre)
        self.__superheroe=superheroe
        self.__editorial=editorial

    def __str__(self):
        return f"\nNombre: {self.__nombre}\nSuperheroe: {self.__superheroe}\nEditorial: {self.__editorial}"

futbolista1 = Futbolista("Lamine Yamal", 1.78, "Madrid", 18, 24)
anime1 = Anime("Novea","charmander","nidea")
superheroe1 = Superheroe("Batman","nose", "Marvel")

print(futbolista1)
print(anime1)
print(superheroe1)

lista = [futbolista1,anime1,superheroe1]

Persona.verLista(lista)