class Persona():
    def __init__(self,nombre,apellido):
        self._nombre = nombre
        self._apellidos = apellido

class Funcionario():
    def __init__(self,cuerpo):
        self._cuerpo = cuerpo

class Profesor(Persona,Funcionario):
    def __init__(self,nombre,apellido, cuerpo):
        super().__init__(nombre,apellido)
        Funcionario.__init__(self, cuerpo)

    def __str__(self):
        return self._apellidos+ ", "+self._nombre+" ("+self._cuerpo+")"


profe1 = Profesor("Carlos","Martín","Policía")

print(profe1) # sale por pantalla el metodo magico __str__

