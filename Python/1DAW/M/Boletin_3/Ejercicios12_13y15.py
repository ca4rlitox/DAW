"""12. Las matrículas españolas constan de un número de cuatro dígitos y tres letras
cualesquiera en mayúsculas a excepción de las vocales, la Ñ y la Q. Escribe un
programa que detecte si una matrícula introducida por teclado es válida o no.
"""
"""
matricula=input("Introduce los 4 numeros y tres letras de su matricula (todo junto sin guiones)")
longitud=len(matricula)
numeros=matricula[:4]
letras=matricula[4:]
letrasMayuscula=letras.upper()
if longitud==7:
    if numeros.isdigit()==True:
        if letrasMayuscula.isalpha()==True:
            print("matricula valida")
        else:
            print("matricula invalida")
    else:
        print("matricula invalida")
else:
    print("matricula invalida")
"""

"""13. Modifica el programa anterior contemplando que entre los números y las letras
podría haber un espacio en blanco (uno solo) o un guión. En ambos casos se
considerará también que la matrícula es válida (si cumple todo lo demás, claro)
"""
"""
matricula=input("Introduce su matricula")
longitud=len(matricula)
numeros=matricula[:4]
letras=matricula[-3:]
espacioGuion=matricula[4]
letrasMayuscula=letras.upper()
if longitud==7:
    if numeros.isdigit()==True:
        if letrasMayuscula.isalpha()==True:
            print("matricula valida")
        else:
            print("matricula invalida")
    else:
        print("matricula invalida")
elif longitud==8:
    if numeros.isdigit()==True:
        if letrasMayuscula.isalpha()==True:
            if espacioGuion==" " or espacioGuion=="-":
                print("matricula valida")
            else:
                print("matricula invalida")
        else:
            print("matricula invalida")
    else:
        print("matricula invalida")
else:
    print("matricula invalida")
"""
"""
15. Escribe un programa que reciba por teclado una fecha en el formato DD/MM/YYYY. El
programa debe de comprobar si la fecha es correcta teniendo en cuenta:
Qué el formato sea el correcto
Que la fecha sea totalmente válida teniendo en cuenta incluso los años que son
bisiestos (aquellos que son divisibles entre cuatro).
"""

fecha=input("Introduce la fecha en formato DD/MM/YYYY ")

longitud=len(fecha)
dia=fecha[:2]
mes=fecha[3:5]
anio=fecha[6:]
barras=fecha[2]+fecha[5]

if longitud==10:
    if barras=="//" :
        if dia.isdigit()==True and mes.isdigit()==True and anio.isdigit()==True:
            dia=int(dia)
            mes=int(mes)
            anio=int(anio)
            if (dia<=31 and dia>0) and (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
                print("La fecha es correcta")
            elif (dia<=30 and dia>0) and (mes==4 or mes==6 or mes==9 or mes==11):
                print("la fecha es correcta")
            elif (dia<=28 and dia>0) and mes==2:
                print("La fecha es correcta")
            elif (dia==29) and (anio%4==0):
                print("La fecha es correcta")
            else :
                print("La fecha es incorrecta")
        else:
            print("La fecha es incorrecta")
    else:
        print("El formato es incorrecto")
