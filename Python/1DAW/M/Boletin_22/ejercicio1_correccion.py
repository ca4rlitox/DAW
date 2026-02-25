from datetime import date
import random

liga={"Real Betis CF":[0,0,0,0,0,0,0],
      "Atlético de Madrid":[0,0,0,0,0,0,0],
      "Sevilla":[0,0,0,0,0,0,0],
      "Barcelona FC":[0,0,0,0,0,0,0],
      "Rayo Vallecano":[0,0,0,0,0,0,0],
      "Real Madrid FC":[0,0,0,0,0,0,0]}

equipos=list(liga.keys())

def resultadosPartido(equipo, golesAFavor, golesEnContra):
    #forma del profe
    """resultados=liga[equipo]
    resultados[5]+=golesAFavor
    resultados[6]+=golesEnContra
    liga[equipo]=resultados"""
    #mi forma
    liga[equipo][5]=golesAFavor
    liga[equipo][6]=golesEnContra
    liga[equipo][1]+=1
    if golesAFavor > golesEnContra:
        liga[equipo][2]+=1
        liga[equipo][0]+=3
    elif golesAFavor < golesEnContra:
        liga[equipo][4]+=1
    else:
        liga[equipo][3]+=1
        liga[equipo][0]+=1


def equiposDelPartido(equipo1,equipo2,golesLocal,golesVisitante):
    equipoLocal=""
    equipoVisitante=""
    for equipo in equipos:
        if equipo1==equipo:
            equipoLocal=equipo
        elif equipo2==equipo:
            equipoVisitante=equipo
    #equipoLocal=liga.get(equipo1) #asi puedo obtener los valores
    #equipoVisitante=liga.get(equipo2) #asi puedo obtener los valores


    resultadosPartido(equipoLocal,golesLocal,golesVisitante)
    resultadosPartido(equipoVisitante,golesVisitante,golesLocal)

def verClasificacion(liga):
    hoy=date.today()
    fecha=hoy.strftime("%d-%m-%y")
    print("-----------------------------------------------------------------")
    print(f" Competicion: La Liga eaSports - Clasificación a día {fecha}")
    print("-----------------------------------------------------------------")
    print(f" {'EQUIPO':<24}|{'Pts':^5}|{'PJ':^4}|{'PG':^4}|{'PE':^4}|{'PP':^4}|{'GF':^4}|{'GC':^4}")
    print("-----------------------------------------------------------------")
    for equipo, valores in liga.items():
        print(f"{equipo:<25}|{valores[0]:>5}|{valores[1]:>4}|{valores[2]:>4}|{valores[3]:>4}|{valores[4]:>4}|{valores[5]:>4}|{valores[6]:>4}")
    #forma del profe
    """for equipo in liga:
        stats=liga.get(equipo)"""


equipo1=equipos[random.randint(0,len(equipos)-1)]
equipo2=equipos[random.randint(0,len(equipos)-1)]
while equipo1==equipo2:
    equipo2=equipos[random.randint(0,len(equipos)-1)]

goles1=random.randint(0,5)
goles2=random.randint(0,5)
equiposDelPartido(equipo1,equipo2,goles1,goles2)

verClasificacion(liga)