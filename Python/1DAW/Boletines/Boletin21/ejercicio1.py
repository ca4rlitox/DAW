from datetime import datetime,timedelta

primeraCita = datetime.now()
primeraCitaaString = primeraCita.strftime("%d del %m de %Y a las %H:%M")
print(f"Registro y primera cita: {primeraCitaaString}")
for i in range (1,7):
    primeraCita = primeraCita+timedelta(days=200)
    primeraCitaaString = primeraCita.strftime("%d del %m de %Y")
    print(f"{i} - {primeraCitaaString}")