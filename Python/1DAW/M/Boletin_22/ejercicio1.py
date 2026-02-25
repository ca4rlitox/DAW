from datetime import date
import random

liga=[["Real Betis CF",0,0,0,0,0,0,0],
      ["Atlético de Madrid",0,0,0,0,0,0,0],
      ["Sevilla",0,0,0,0,0,0,0],
      ["Barcelona FC",0,0,0,0,0,0,0],
      ["Rayo Vallecano",0,0,0,0,0,0,0],
      ["Real Madrid FC",0,0,0,0,0,0,0]]


def partidosJugados(equipo1,equipo2):
    for eq in liga:
        if eq[0]==equipo1:
            eq[2]+=1
        if eq[0]==equipo2:
            eq[2]+=1

def partidosGanados(equipo):
    for eq in liga:
        if eq[0]==equipo:
            eq[3]+=1
            eq[1]+=3

def partidosPerdidos(equipo):
    for eq in liga:
        if eq[0]==equipo:
            eq[5]+=1
def partidosEmpatados(equipo1,equipo2):
    for eq in liga:
        if eq[0]==equipo1 or eq[0]==equipo2:
            eq[4]+=1
            eq[1]+=1
def golesAFavor(equipo,goles):
    for eq in liga:
        if eq[0]==equipo:
            eq[6]+=goles
def golesENContra(equipo,goles):
    for eq in liga:
        if eq[0]==equipo:
            eq[7]+=goles

def resultadosPartido(equipo1,equipo2,goles1,goles2):
    partidosJugados(equipo1,equipo2)
    golesAFavor(equipo1,goles1)
    golesAFavor(equipo2,goles2)
    golesENContra(equipo1,goles2)
    golesENContra(equipo2,goles1)
    if goles1>goles2:
        partidosGanados(equipo1)
        partidosPerdidos(equipo2)
    elif goles2>goles1:
        partidosGanados(equipo2)
        partidosPerdidos(equipo1)
    else:
        partidosEmpatados(equipo1,equipo2)


def verClasificacion(liga):
    lineas="-----------------------------------------------------------------"
    longitud=len(lineas)
    hoy=date.today()
    fecha=hoy.strftime("%d-%m-%y")
    cabecera=f"Competicion: La Liga eaSports - Clasificación a día {fecha}"
    print("-----------------------------------------------------------------")
    print(" ",cabecera)
    print("-----------------------------------------------------------------")
    print(f" {'EQUIPO':<24}|{'Pts':^5}|{'PJ':^4}|{'PG':^4}|{'PE':^4}|{'PP':^4}|{'GF':^4}|{'GC':^4}")
    print("-----------------------------------------------------------------")
    for equipo in liga:
        print(f"{equipo[0]:<25}|{equipo[1]:>5}|{equipo[2]:>4}|{equipo[3]:>4}|{equipo[4]:>4}|{equipo[5]:>4}|{equipo[6]:>4}|{equipo[7]:>4}")
verClasificacion(liga)

equipo1=liga[random.randint(0,5)][0]
equipo2=liga[random.randint(0,5)][0]
while equipo1==equipo2:
    equipo2=liga[random.randint(0,5)][0]

goles1=random.randint(0,5)
goles2=random.randint(0,5)
resultadosPartido(equipo1,equipo2,goles1,goles2)

verClasificacion(liga)