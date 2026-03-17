from datetime import date,datetime,time,timedelta
from Conductor import Conductor
from Moto import Moto

hola = datetime.today().strftime("%Y")

conductor1 = Conductor("Carlos","5454h","20/04/2004",2024,8)
moto1 = Moto(conductor1,"6807GRZ",2004)

moto1.calcularSeguro()