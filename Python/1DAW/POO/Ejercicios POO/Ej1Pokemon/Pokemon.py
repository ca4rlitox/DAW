import random

class Pokemon:
    #Duda: ¿Cómo admito solo dos atributos de tipo?
    def __init__(self,codigo,nombre,peso1,peso2,altura1,altura2,*tipos):
        self.codigo = codigo
        self.nombre = nombre

        if peso2 > peso1:
            self.peso = random.randint(peso1,peso2)
        else:
            self.peso = random.randint(peso2,peso1)

        if altura2 > altura1:
            self.altura = random.randint(altura1,altura2)
        else:
            self.altura = random.randint(altura2,altura1)

        self.tipos = tipos

        if len(self.tipos) > 2:
            raise AttributeError

    @property
    def verTipos(self):
        if len(self.tipos) == 1:
            return self.tipos[0]
        else:
            return f"{self.tipos[0]}, {self.tipos[1]}"

    def verDatos(self):
            print(f"Código {self.codigo}, nombre: {self.nombre}, peso: {self.peso}, altura: {self.altura}, tipo/s: {self.verTipos}")

class Entrenador(Pokemon):
    def __init__(self,codigo,nombre,peso1,peso2,altura1,altura2,*tipos):
        super().__init__(codigo, nombre, peso1, peso2, altura1, altura2, *tipos)

    def verDatos(self):
        print(f"Código {self.codigo}, nombre: {self.nombre}, peso: {self.peso}, altura: {self.altura}, tipo/s: {self.verTipos}")


class Equipo:
    def __init__(self,entrenador,pokemon1,pokemon2,pokemon3):
        self.entrenador = entrenador
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.pokemon3 = pokemon3

    def verDatos(self):
        Entrenador.verDatos(self.entrenador)
        Pokemon.verDatos(self.pokemon1)
        Pokemon.verDatos(self.pokemon2)
        Pokemon.verDatos(self.pokemon3)
