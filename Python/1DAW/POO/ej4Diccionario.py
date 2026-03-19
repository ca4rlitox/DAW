class Tarea:
    __listaTareas = {}
    def __init__(self,identificador,titulo,prioridad):
        self.__id = identificador
        self.__titulo = titulo
        self.__prioridad = prioridad
        self.__completada = False
        if identificador in Tarea.__listaTareas:
            print("La tarea ya existe")
        else:
            Tarea.__listaTareas[identificador] = self


    @classmethod
    def mostrarTareasNoCompletadas(cls):
        print("Lista de tareas:")
        for tarea in cls.__listaTareas:
            print(f"[{tarea.__id}]")

    @classmethod
    def marcarComoCompletada(cls,id):
        if id in Tarea.__listaTareas:
            tarea = cls.__listaTareas[id]
            tarea.__completada = True
            print("Tarea marcada como completada.")
        else:
            print("La tarea",id,"no existe.")

t1 = Tarea("P43","Comprar pollo", 9)
t3 = Tarea("p47","Comprar pollo", 9)
t2 = Tarea("P43","Duolingo", 4)

print(t1.mostrarTareasNoCompletadas)
t1.marcarComoCompletada(t1)
