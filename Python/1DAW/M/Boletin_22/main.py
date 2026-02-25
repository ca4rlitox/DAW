from datetime import datetime

# Índices para que el código sea legible
EQUIPO = 0
PTS = 1
PJ = 2
PG = 3
PE = 4
PP = 5
GF = 6
GC = 7

# Liga inicial
liga = [
    ["Real Betis CF", 0, 0, 0, 0, 0, 0, 0],
    ["Atlético de Madrid", 0, 0, 0, 0, 0, 0, 0],
    ["Sevilla", 0, 0, 0, 0, 0, 0, 0],
    ["Barcelona FC", 0, 0, 0, 0, 0, 0, 0],
    ["Rayo Vallecano", 0, 0, 0, 0, 0, 0, 0],
    ["Real Madrid FC", 0, 0, 0, 0, 0, 0, 0]
]


def buscar_equipo(nombre):
    for equipo in liga:
        if equipo[EQUIPO] == nombre:
            return equipo
    return None


def resultadosPartido(equipo1, equipo2, goles1, goles2):
    eq1 = buscar_equipo(equipo1)
    eq2 = buscar_equipo(equipo2)

    if not eq1 or not eq2:
        print("❌ Equipo no encontrado")
        return

    # Partidos jugados
    eq1[PJ] += 1
    eq2[PJ] += 1

    # Goles
    eq1[GF] += goles1
    eq1[GC] += goles2
    eq2[GF] += goles2
    eq2[GC] += goles1

    # Resultado
    if goles1 > goles2:
        eq1[PTS] += 3
        eq1[PG] += 1
        eq2[PP] += 1
    elif goles1 < goles2:
        eq2[PTS] += 3
        eq2[PG] += 1
        eq1[PP] += 1
    else:
        eq1[PTS] += 1
        eq2[PTS] += 1
        eq1[PE] += 1
        eq2[PE] += 1


def mostrar_clasificacion():
    fecha = datetime.now().strftime("%d-%m-%y")

    print("-" * 65)
    print(f"Competición: La Liga eaSports - Clasificación a día {fecha}")
    print("-" * 65)
    print("EQUIPO                 | Pts | PJ | PG | PE | PP | GF | GC")
    print("-" * 65)

    liga_ordenada = sorted(
        liga,
        key=lambda e: (e[PTS], e[GF] - e[GC]),
        reverse=True
    )

    for equipo in liga_ordenada:
        print(f"{equipo[EQUIPO]:22} | {equipo[PTS]:3} | {equipo[PJ]:2} | "
              f"{equipo[PG]:2} | {equipo[PE]:2} | {equipo[PP]:2} | "
              f"{equipo[GF]:2} | {equipo[GC]:2}")