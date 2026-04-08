class Persona():
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellidos = apellido

class Funcionario():
    def __init__(self,cuerpo):
        self.cuerpo = cuerpo

class Profesor(Persona,Funcionario):
    def __init__(self,nombre,apellido, cuerpo):
        super().__init__(nombre,apellido)
        Funcionario.__init__(self, cuerpo)

    # Paso 2: tengo que crear una función que se llame igual que el decorador que creamos y le pasamos como argumento otra función, y devuelve una funcion
    # recibe como argumento la funcion que aparece debajo del decorador. (funcion=saludo)

    def mi_decorador(funcion):
        # aqui dentro hacemos la otra funcion que tiene que devolver
        def envoltorio(self):
            print("Buenos días cuerpo de", self._cuerpo)  # esto es la decoración, es opcional
            funcion  # el momento que queremos que se ejecute nuestra función
            print("Que tengas un buen día")  # otra decoración

        return envoltorio

    # creamos un decorador
    @mi_decorador
    def saludo(self):
        print("Hola ", self._nombre)

profe1 = Profesor("Carlos","Martín","Policía")


profe1.mi_decorador()