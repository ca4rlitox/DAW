#COMO FUNCIONAN LAS CLASES DE FECHA Y DE HORAS EN PYTHON

from datetime import date, time, datetime, timedelta #importamos la libreria

#CLASE DATE

hoy=date.today() #el metodo date.today me devuelve la fecha de hoy (en formato anglosajon)
print(hoy)

#quiero crear una fecha específica

cumple= date(1968,10,8) #pongo entre paréntesis el año, mes y dia
#cumple2=date(1968) #tengo que especificar la fecha completamente sino me da un error
print(cumple)

#TIME para horas, pero no puedo poner la fecha actual con time

hora=time(14,30,45)
hora2=time(14) #aqui si puedo no específicar minutos y segundos
print(hora)
print(hora2)
#DATETIME para fecha y hora , si puedo poner la fecha actual con datetime.now() aunque la fecha no me sirva

ahora=datetime.now()
print(ahora)

citaMedico=datetime(2026,2,11,14,56) #si no quiero algun valor lo mejor es rellenar con 0
print(citaMedico)



#FORMATEAR LA FECHA PARA ESPAÑOL

citaFormateada=citaMedico.strftime("%d/%m/%y a las %H:%M") #metodo que me sirve para dar formato a la fecha, puedo ponerle texto ademas quitando el %
                                                            #el % es un código y las minúsculas d m y son dias mes y años, H y M en mayusculas horas y minutos
                                                            #con y el año aparece con 2 cifras, y con Y (mayuscula) aparece todo el año
print(citaFormateada)

citaFormateada2=citaMedico.strftime("%A (%w) %d/%m/%y a las %H:%M") #con %A aparece el nombre del día en ingles, (a minuscula el día abreviado)
                                                                    # %w es el número del día de la semana (miercoles/wednesday=3)

hoyFormateado=hoy.strftime("%a %d/%m/%y a %H:%M") #como es date, no puede poner horas. aparecen en 0
print(hoyFormateado)

"""<<<<<<<<<<<<convertir de texto a objeto de fecha y hora>>>>>>>>>>>>>>>>>>>"""

fecha= "01 12 2025"

objetoFecha= datetime.strptime(fecha,"%d %m %Y") #strptime me convierte la cadena a objeto fecha, es importante que los separadores sean iguales
print(objetoFecha)

#OPERACIONES CON FECHAS

#me soluciona las operaciones aritmeticas con fechas, las hace automaticamente sin importar año bisisto, mes de 28 dias, etc

#me tengo que asegurar que sean objetos del mismo tipo


#puedo compararlos con mayor, menor, igual, etc
hoy2=datetime.now()
if hoy2 < objetoFecha:
    print(hoy2," es anterios a", objetoFecha)
else:
    print(objetoFecha," es anerior a",hoy2)

#TIMEDELTA (CLASE IMPORTADA)

dentroDe67Dias= hoy2 + timedelta(weeks=2, days=67, hours=4, seconds=33) #puedo sumar o restar y me muestra la fecha del tiempo que indico
print(dentroDe67Dias)