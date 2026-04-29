class Pregunta:
    def __init__(self,pregunta,respuesta1,respuesta2,respuesta3):
        self.__pregunta = pregunta
        self.__lista_respuestas = [respuesta1,respuesta2,respuesta3]

    def __str__(self):
        return f"{self.__pregunta} A) {self.__lista_respuestas[0]} B) {self.__lista_respuestas[1]} C) {self.__lista_respuestas[2]}"

class Examen:
    def __init__(self):
        self.__listaPregunta = []

    def addPregunta(self,p):
        self.__listaPregunta.append(p)

    def hacerExamen(self):
        correctas=0
        if len(self.__listaPregunta) > 0:
            for i in self.__listaPregunta:
                respuesta = input(f"{i}\nIntroduce la respuesta: ")
                if respuesta.upper() == "A":
                    correctas+=1
                elif respuesta.upper() != "A" or respuesta.upper() != "B" or respuesta.upper() != "C":
                    while respuesta.upper() != "A" and respuesta.upper() != "B" and respuesta.upper() != "C":
                        print("Introduce una respuesta valida")
                        respuesta = input(f"{i}\nIntroduce la respuesta: ")
                        if respuesta.upper() == "A":
                            correctas += 1

            if correctas==0:
                print("No hay respuestas correctas")
            else:
                print(f"Hay {correctas} preguntas correctas")

pregunta1 = Pregunta("Esta permitido atropellar peatones?","No","Si esta justificado","Si")

examen1 = Examen()

examen1.addPregunta(pregunta1)
examen1.addPregunta(pregunta1)
examen1.addPregunta(pregunta1)

examen1.hacerExamen()