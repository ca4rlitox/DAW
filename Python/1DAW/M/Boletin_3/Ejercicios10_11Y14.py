"""10. Escribe un programa que valide si un NIF español introducido por teclado es correcto.
La longitud exacta de la cadena ha de ser de 9 caractéres. Los ocho primeros han de
ser números comprendidos entre el 0 y el 9 y el último una letra que puede estar
escrita en mayúsculas o minúsculas.
"""
"""
nif=input("Introduce su NIF ")

longitud=len(nif)
numeros=nif[:8]
letra=nif[8:]
letraMayus=letra.upper()

if longitud==9:
    if numeros.isdigit()==True:        
        if letraMayus.isalpha()==True:
            print("el NIF ingresado es correcto")
        else:
            print("el NIF ingresado es incorrecto")
    else:
        print("el NIF ingresado es incorrecto")
else:
    print("el NIF ingresado es incorrecto")
"""
"""11. Mejorar el programa anterior para que detecte si se trata de un NIF o un NIE y nos
comunique, además de si es válido de que tipo es.
Un NIE es una cadena de 9 caractéres que siempre empieza por X,Y o Z y a
continuación vienen 7 cifras y una letra final. Las letras inicial y final pueden estar
escritas con mayúsculas o con minúsculas
"""
"""
nifNie=input("Introduce su NIF/NIE ")
longitud=len(nifNie)
numerosnif = nifNie[:8]
numerosnie = nifNie[1:8]
letraFinal = nifNie[8:]
letraIncio = nifNie[0]
letraFinalMayus = letraFinal.upper()
letraIncioMayus = letraIncio.upper()


if longitud==9:
    if numerosnif.isdigit()==True:
        if letraFinalMayus.isalpha()==True:
            print("el NIF ingresado es correcto")
        else:
            print("el NIF ingresado es incorrecto")
    elif numerosnie.isdigit()==True:
        if letraFinalMayus.isalpha()==True:
            if letraIncioMayus=="X" or letraIncioMayus=="Y" or letraIncioMayus=="Z":
                print("el NIE ingresado es correcto")
            else:
                print("el NIE ingresado es incorrecto")
        else:
            print("el NIE ingresado es incorrecto")
    else:
        print("el NIF/NIE ingresado es incorrecto")
else:
    print("el NIF/NIE ingresado es incorrecto")
"""
"""14. Modifica el programa que validaba si un NIF era correcto comprobando si la letra que
incorpora lo es.Para calcular la letra del DNI, debes dividir el número del DNI entre 23
y tomar el resto de esa división. Luego, busca ese número de resto en la tabla de 
equivalencia de letras para encontrar la letra correcta"""

nif=input("Introduce su NIF ")

longitud=len(nif)
numeros = nif[:8]
letra = nif[8:]
letraMayus = letra.upper()
letraCorregida="A"
if longitud==9:
    if numeros.isdigit()==True:
        numNif= int (numeros)
        resto=numNif%23
        if letraMayus.isalpha()==True:
            match resto:
                case 0:
                    letraCorregida="T"
                case 1:
                    letraCorregida="R"
                case 2:
                    letraCorregida="W"
                case 3:
                    letraCorregida="A"
                case 4:
                    letraCorregida="G"
                case 5:
                    letraCorregida="M"
                case 6:
                    letraCorregida="Y"
                case 7:
                    letraCorregida="F"
                case 8:
                    letraCorregida="P"
                case 9:
                    letraCorregida="D"
                case 10:
                    letraCorregida="X"
                case 11:
                    letraCorregida="B"
                case 12:
                    letraCorregida="N"
                case 13:
                    letraCorregida="J"
                case 14:
                    letraCorregida="Z"
                case 15:
                    letraCorregida="S"
                case 16:
                    letraCorregida="Q"
                case 17:
                    letraCorregida="V"
                case 18:
                    letraCorregida="H"
                case 19:
                    letraCorregida="L"
                case 20:
                    letraCorregida="C"
                case 21:
                    letraCorregida="K"
                case 22:
                    letraCorregida="E"

            if(letraMayus==letraCorregida):
                print("el NIF ingresado es correcto")
            else:
                print("el NIF ingresado es incorrecto")
        else:
            print("el NIF ingresado es incorrecto")
    else:
        print("el NIF ingresado es incorrecto")
else:
    print("el NIF ingresado es incorrecto")