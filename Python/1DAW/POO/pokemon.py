class Pokemon:
    numPokemon=0
    @classmethod
    def coleccion(cls):
        print(f"Tienes {cls.numPokemon} pokemons en tu colección")
    #Para indicar que puede tener muchos atributos, se pone delante un asterisco
    def __init__ (self,numPokedex,nombre,*tipos):
        self.__nombre = nombre
        self.__numPokedex = numPokedex
        self.__tipos = tipos
        Pokemon.numPokemon+=1

    @property
    def nombre(self):
        return self.__nombre

    def verPokemon(self):
        print(f"#{self.__numPokedex} - {self.__nombre}")
        print(f"  Tipos {self.__tipos}")
