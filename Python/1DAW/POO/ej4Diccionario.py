class listaTareas:
    def __init__(self,identificador,titulo,prioridad,estaRealizada):
        self.diccionario = {}
        self.identificador = identificador
        self.titulo = titulo
        self.prioridad = prioridad
        self.estaRealizada = estaRealizada
        self.diccionario+= {self.identificador, self.titulo, self.prioridad, True}



hola = listaTareas("P43","Marica",9,True)

