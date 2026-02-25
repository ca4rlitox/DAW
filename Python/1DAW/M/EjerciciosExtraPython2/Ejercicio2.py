from datetime import datetime

lista = [
    "01/01/2020",
    "15/08/2025",
    "31/12/99",
    "29/02/2024",
    "29/02/2023",
    "hola",
    "10/10/10",
    "01/01/2050"
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

def pasadas_futuras(fechas):
    pasadas=[]
    futuras=[]
    hoy=datetime.today().date()
    for f in fechas:
        if f > hoy: #ambos son objetos de tipo date por eso puedo comparar
            futuras.append(f)
        elif f < hoy:
            pasadas.append(f)
    print("Fechas pasadas ")
    for f in pasadas:
        print(f)
    print("fechas futuras")
    for f in futuras:
        print(f)

def comprueba_fechas(fechas):
    fechaValida=[]
    for fecha in fechas:
        fechaConvertida=fecha_valida(fecha) #tengo que convertir en objeto para poder comparar luego
        if fechaConvertida: #los objetos de por si funcionan como un true si existen, si es None (no existe) es como un false
            fechaValida.append(fechaConvertida)
    pasadas_futuras(fechaValida)

comprueba_fechas(lista)