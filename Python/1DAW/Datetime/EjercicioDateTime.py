from datetime import date,time,timedelta

hora= time(14,3).strftime("%H:%M")
cita = date.today().strftime("%d del %m de %Y a las ")

citaYhora = cita+str(hora)

print("\nRegistro y primera cita:", citaYhora)
print("Siguientes citas:")

hoy = date(2026,2,4)
for i in range(1,7,1):
    programadas = timedelta(200) + hoy
    hoy = programadas
    enElprint = programadas.strftime("%d del %m de %Y")
    print(i,"-",enElprint)
