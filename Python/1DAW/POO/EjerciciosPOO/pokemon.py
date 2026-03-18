class Pokemon:
    numPokemon=0
    @classmethod
    def coleccion(cls):
        print(f"Tienes {cls.numPokemon} pokemons en tu colección")

    #Para indicar que puede tener muchos atributos de un mismo tipo, se pone delante un asterisco
    def __init__ (self,numPokedex,nombre,*tipos):
        self.__nombre = nombre
        self.__numPokedex = numPokedex
        self.__tipos = tipos
        Pokemon.numPokemon+=1

    #Getter
    @property
    def nombre(self):
        return self.__nombre

    def verPokemon(self):
        print(f"#{self.__numPokedex} - {self.__nombre}")
        print(f"  Tipos {self.__tipos}")

        # Herencia
class PokemonLegendario(Pokemon):
    def __init__(self,num,nombre,*tipos):
        super().__init__(num,nombre,*tipos)

    def verPokemon(self):
        print("Pokemon legendario: ")
        super().verPokemon()
