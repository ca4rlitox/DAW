from datetime import datetime

class Persona:
    def __init__(self,nombre,apellidos):
        self._nombre = nombre
        self._apellidos = apellidos

class Medico(Persona):
    def __init__(self, nombre, apellidos, especialidad, numColegiado, centroMedico):
        super().__init__(nombre, apellidos)
        self.__especialidad = especialidad
        if len(str(numColegiado)) == 6:
            self.__numColegiado = str(numColegiado)
        else:
            print("Error al establecer el numero de colegiado. Solo debe tener 6 caracteres.")
        self.__centroMedico = centroMedico

    def __str__(self):
        return f"Nombre médico: {self._nombre} {self._apellidos} con número de colegiado {self.__numColegiado}. Especialidad: {self.__especialidad}. Centro medico: {self.__centroMedico.getNombreCentro}"
    @property
    def getNombreMedico(self):
        return self._nombre+" "+self._apellidos

class Paciente(Persona):
    def __init__(self, nombre, apellidos, dni, telefono):
        super().__init__(nombre, apellidos)
        self.__dni = dni
        self.__telefono = telefono

    def __str__(self):
        return f"Nombre paciente: {self._nombre} {self._apellidos} con número de DNI {self.__dni} y teléfono {self.__telefono}"

class CentroMedico:
    def __init__(self,nombre,codigo,centroMedico):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__centroMedico = centroMedico
        self.__medicos = []
        self.__pacientes = []

    def addCentroMedico(self,paciente,centroMedico):
        self.__pacientes.append(paciente)

    def cambiarCentroPaciente(self,paciente,nuevoCentroMedico):
        if paciente in self.__pacientes:
            self.__pacientes.remove(paciente)
            self.addCentroMedico(paciente,nuevoCentroMedico)
        else:
            print("No se ha eliminado el registro porque no se ha encontrado...")

    @property
    def getNombreCentro(self):
        return self.__nombre
    def addMedico(self, medico):
        self.__medicos.append(medico)
    def addPaciente(self, paciente):
        self.__pacientes.append(paciente)

    def obtenerMedicos(self,centroMedico):
        print("Centro médico", self.__nombre, "lista de médicos:")
        for i in self.__medicos:
            print(i)
    def obtenerPacientes(self,centroMedico):
        print("Centro médico", self.__nombre, "lista de pacientes:")
        for i in self.__pacientes:
            print(i)

class Consulta:
    def __init__(self,motivo,consejoMedico, medicoAsignado, paciente):
        self.__localDate = datetime.today()
        self.__motivo = motivo
        self.__consejoMedico = consejoMedico
        self.__medicoAsignado = medicoAsignado
        self.__paciente = paciente

    def __str__(self):
        return (f"Paciente: {self.__paciente} Fecha y hora de la consulta: {self.__localDate.strftime("%d/%m/%Y a las %H:%M")}.\nMotivo de la consulta: {self.__motivo} consejo médico {self.__consejoMedico}. Médico:"
                f"{self.__medicoAsignado.getNombreMedico}")

centroMedico1 = CentroMedico("Francisco Franco", "7847", "4")
medico1 = Medico("Carlos", "Martin", "Medicina interna", "654878", centroMedico1)
medico2 = Medico("Pepe", "Codina", "Medicina externa", "874175", centroMedico1)
paciente1 = Paciente("Fran", "Estremo", "0511454G", "654878")

centroMedico1.addMedico(medico1)
centroMedico1.addMedico(medico2)
centroMedico1.addPaciente(paciente1)
centroMedico1.obtenerMedicos("7847")
centroMedico1.obtenerPacientes("7847")

primeraConsulta = Consulta("VIH","tomar pipas",medico1,paciente1)

print(primeraConsulta)

