from datetime import datetime,date,time

fechasSupuestamente = ["13/02/25", "hola carmela", "12 34 56", "14/06/2026", "bra, bra", "56/13/26"]
fechasValidas = []
fechasInvalidas = []
hola = False

while hola:
    try:
        for fechas in fechasSupuestamente:
            if isinstance(fechas,date):
                fechasValidas.append(fechas)
        else:
            fechasInvalidas.append(fechas)
            hola = True
    except:
        print("vagabundo")


print(fechasInvalidas)
print(fechasValidas)

