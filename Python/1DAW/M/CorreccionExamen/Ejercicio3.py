"""Queremos hacer un programa en Python que construya una cadena de texto a partir de otras dos
ya existentes (y que no se meten por teclado, sino que tienen que estar definidas como variables en
tu código). Las cadenas cuentan con la siguiente estructura:
 -La primera de ellas tiene dos palabras separadas por un espacio en blanco
 -La segunda tiene dos palabras separadas por un guión
 Tu cadena resultante debería de hacer una composición con esos dos textos y mostrar, al final, la
longitud total de ambas cadenas entre paréntesis como se verá en el ejemplo que sigue.
Suponiendo que las dos cadenas de las que se parte son las siguientes:
 texto1 = “Examen 1T01”;
 texto2 = “Octubre-2025”;
La ejecución de tu programa debería de mostrar esto:
 Resultado: 1T01-2025 Examen Octubre (24)
 Como ves, aparecen primero las palabras que van en segundo lugar de ambas separadas por un
guión y luego las palabras que van en primer lugar separadas por un espacio. Finalmente, un
paréntesis con la longitud total que suman ambas.
 NOTAS IMPORTANTES:
 -Ambas cadenas cumplen con el formato que se pide, es decir, son dos palabras separadas
por un espacio y un guión respectivamente.
 -Tu programa no solo debe de producir la salida que se pide por consola, sino que tiene que
producir y almacenar una tercera variable de tipo String con el contenido que luego se
muestra en consola."""

texto1 = "Examen 1T01"
texto2 = "Octubre-2025"

#longitud=len(texto1+texto2)
posicion = texto1.index(" ") #aqui con index hago un "corte" entonces posicion siempre sera hasta el espacio sin importar cuantos caracteres haya antes o despues
posicionDos = texto2.index("-")

uno= texto1[:posicion+1] #aqui tengo la primera parte del texto, hasta la posicion del espacio
dos=texto1[posicion+1:] #y aqui  la segunda parte desde posicion+1 (para que no cuente el espacio) hasta el final del texto

tres= texto2[:posicionDos]
cuatro= texto2[posicionDos:]

resultado=dos+cuatro+" "+uno+tres
longitud=len(resultado)

print(resultado," (",longitud,")",sep="")
