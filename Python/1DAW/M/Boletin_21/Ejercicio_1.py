"""Tienes que hacer un programa para un taller de coches. Una vez que pasas una revisión, se programan las
seis siguientes con un intervalo de 200 días cada uno. La salida por consola sería algo así:
Registro y primera cita: 4 del 02 de 2026 a las 17:47
Siguientes citas:
1 - 23 del 08 de 2026
2 – 11 del 08 de 2027
3 – 27 del 12 del 2027
4 – 14 del 04 de 2028
5 – 31 del 10 de 2028
6 – 19 del 05 de 2029
Para tomar la fecha del registro y primera cita se toma la fecha y hora del momento en que se lanza el
programa"""

from datetime import date, datetime, timedelta

fecha=date.today()
registro=datetime.now()
print("Registro y primera cita:",registro.strftime("%d del %m de %Y a las %H:%M"))

print("Siguientes citas:")
for i in range(6):
    siguienteCita=fecha+timedelta(days=200)
    print(i+1,"-",siguienteCita.strftime("%d del %m de %Y"))
    fecha=siguienteCita