class Conductor:
    def __init__(self,nombre,nif,fecha_nacimiento,ano_carnet,puntos):
        self.nombre = nombre
        self.nif = nif
        self.fecha_nacimiento = fecha_nacimiento
        self.ano_carnet = ano_carnet
        self.puntos = puntos
        @property
        def verAnoNacimiento():
            ano = self.fecha_nacimiento
            ano = ano.split("/")
            return ano[2]