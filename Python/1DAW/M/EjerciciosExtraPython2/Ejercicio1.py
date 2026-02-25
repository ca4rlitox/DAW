from datetime import datetime
lista = [
    "01/01/2024",
    "31/12/23",
    "hola",
    "29/02/2024",
    "30/02/2023",
    "15-08-2023",
    "10/10/10"
]
def fecha_valida(fecha):
    formato=["%d/%m/%y","%d/%m/%Y"]
    for f in formato:
        try:
            fecha = datetime.strptime(fecha, f).date()
            return fecha
        except:
            pass
    return None

def comprueba_fechas(fechas):
    fechaValida=[]
    fechaInvalida=[]
    for fecha in fechas:
        if fecha_valida(fecha):
            fechaValida.append(fecha)
        else:
            fechaInvalida.append(fecha)
    print("Fechas Validas")
    for f in fechaValida:
        print(f)
    print("Fechas Invalidas")
    for f in fechaInvalida:
        print(f)
comprueba_fechas(lista)

