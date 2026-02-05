from datetime import date,datetime,time,timedelta

def comprobarFormato(listaConFechas):
    fechasValidas = []
    fechasInvalidas = []
    fecha = datetime.strptime(listaConFechas, "%d/%m/%Y")
    for i in range (len(listaConFechas)):
        try:
            fecha = datetime.strptime(listaConFechas, "%d/%m/%YY")
            fechasValidas.append(fecha.strptime("%d/%m/%YY"))
        except:
            fechasInvalidas.append(listaConFechas)
    return fechasValidas, fechasInvalidas






listaConFechas = []

for i in range(0,2):
    listaConFechas.append(input("Introduce una fecha en formato DD/MM/AAAA o DD/MM/AA: "))
print(comprobarFormato(listaConFechas))