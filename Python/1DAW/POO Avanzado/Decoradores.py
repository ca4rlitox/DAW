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

    def mi_decorador(funcion):
        print("Cuerpo:",Profesor.cuerpo)
        funcion()
        print("Que tengas un buen día")
    @mi_decorador
    def saludo(self):
        print("Hola",self._nombre)

profe1 = Profesor("Carlos","Martín","Policía")


profe1.mi_decorador()