""" Escribe una función que reciba un como argumento un número variable de strings y nos diga,
por cada uno de ellos, si se trata de una matrícula de coche válida.
La matrícula debe de estar formada por cuatro dígitos y tres letras
Las letras Ñ, Q o cualquiera de las vocales no son válidas
Serían, por ejemplo, matrículas inválidas: “22CDR”, “3456BAC” o “1224MN” y serían matrículas
válidas “2222CDR”, “3456BBC” o “1224MNP”
Tú función debe de contemplar que la matrícula puede venir con las letras en mayúsculas o en
minúsculas y debería de darla como válida. También que a veces se escribe separando los números
de las letras con un espacio (pero solo uno) o un guión y también debería de considerarse válido.
Serían válidas, por ejemplo, “7521-MXP”, “6555KFG” o “5432 BCF” pero no lo serían “7521 MXP”
(con cinco espacios entre números y letras) o “5432 – BCF” (con un espacio, un guión y un espacio
entre medios). Es decir: si hay algo entre los números y las letras solo se admite que sea un único
espacio o un único guión.
A continuación dos ejemplos de llamada a la función con sus respectivas salidas en consola:
matriculasValidas(“22CDR”, “7521-MXP” , “1224MN”)
22CDR no es válida
7521-MXP es válida
1224MN no es válida
Matrículas válidas: 1
Matrículas no válidas: 2
matriculasValidas(“5432 – BCF”, “3456BAC”)
5432 – BCF no es válida
3456BAC no es válida
Matrículas válidas: 0
Matrículas no válidas: 2
NOTA: Puedes hacer el ejercicio usando expresiones regulares o no, pero la nota máxima del mismo
solo se obtiene si las usas.
Se valorará también si haces el desarrollo de forma modular usando una función que reciba una
matricula y devuelva un valor booleano diciendo si es válida o no.
"""
import re
matricula=input("Introduce una matrícula: ").upper()

def esMatriculaValida(matricula):
    patron=r'^\d{4}[ -]?[BCDFGHJKLMNPRSTVWXTZ]{3}$'
    return re.match(patron, matricula)

if esMatriculaValida(matricula):
    print("es válida")
else:
    print("no es válida")