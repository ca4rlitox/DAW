from datetime import date

hoy = date.today().strftime("%d-%m-%y")
liga = [["Atlético de Madrid", 0, 0, 0, 0, 0, 0, 0 ],
        ["Real Betis CF", 0, 0, 0, 0, 0, 0, 0 ],
        ["Sevilla", 0, 0, 0, 0, 0, 0, 0 ],
        ["Barcelona FC", 0, 0, 0, 0, 0, 0, 0 ],
        ["Rayo Vallecano", 0, 0, 0, 0, 0, 0, 0 ],
        ["Real Madrid", 0, 0, 0, 0, 0, 0, 0 ]]

def verClasificacion(liga):
    print(f"-----------------------------------------------------------------\n"
    f"   Competición: La Liga eaSports - Clasificación a día {hoy}    \n"
    f"-----------------------------------------------------------------\n"
    f"  {'EQUIPO':20} | {'Pts':^4}|  {'PJ':^2} |  {'PG':^2} |  {'PE':^2} |  {'PP':^2} |  {'GF':^2} |  {'GC':^2}\n"
    f"-----------------------------------------------------------------\n")
    for i in liga:
        print(f"{liga[i][0]}")


def main():
    verClasificacion(liga)

main()

