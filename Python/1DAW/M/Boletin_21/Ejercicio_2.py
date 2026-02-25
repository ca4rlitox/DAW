"""Tenemos una lista con cadenas de texto que, previsiblemente, deberían de ser fechas en formato
dd/mm/yy. Por ejemplo esta:
[“13/02/25”, “hola carmela”, “12 34 56”, “14/06/2026”, “bra, bra”,
“56/13/26”]
La lista puede ser esa o cualquier otra. Usa excepciones para separar las que se trata de fechas correctas de
las que no lo son y muéstrales en consola. Por ejemplo así:
Fechas correctas:
“13/02/25”
“14/06/2026”
Fechas incorrectas:
“hola carmela”
“12 34 56”
“bra, bra”,
“56/13/26”"""

from datetime import datetime

lista = ["13/02/25", "hola carmela", "12 34 56", "14/06/2026", "bra, bra", "56/13/26"]

def es_fecha_valida(cadena):
    """Comprueba si una cadena es una fecha válida en dd/mm/yy o dd/mm/yyyy"""
    formatos = ["%d/%m/%y", "%d/%m/%Y"]

    for formato in formatos:
        try:
            datetime.strptime(cadena, formato)
            return True
        except ValueError:
            pass

    return False


def comprueba_fechas(lista_fechas):
    fechas_validas = []
    fechas_no_validas = []

    for elemento in lista_fechas:
        if es_fecha_valida(elemento):
            fechas_validas.append(elemento)
        else:
            fechas_no_validas.append(elemento)

    print("Fechas correctas:")
    for fecha in fechas_validas:
        print(fecha)

    print("\nFechas incorrectas:")
    for fecha in fechas_no_validas:
        print(fecha)

comprueba_fechas(lista)