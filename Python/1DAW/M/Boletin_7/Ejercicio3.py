"""Pide al usuario un número del 1 al 12 y muestra el nombre del mes correspondiente.
Muestra un error si el número no se corresponde con ningún mes"""

meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre",
        "Octubre","Noviembre","Diciembre"]

num=int(input("Ingrese un número del 1 al 12 para saber el mes que corresponde: "))

if num>=1 and num<=12:
    print(num," corresponde al mes: ",meses[num-1])
else:
    print("Número incorrecto. Tiene que ser entre el 1 y el 12")
