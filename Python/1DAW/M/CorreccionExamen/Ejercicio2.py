"""Tenemos una empresa que trabaja con Cuba, India y Suiza y necesitamos hacer un programa en
Python que nos permita hacer cambios de moneda entre Euros, pesos cubanos, Rupias y Francos 
Suizos. Los cambios actuales entre estas monedas son los siguientes:
- 1 Euro equivale a 27,93 pesos cubanos
- 1 Euro equivale a 102,81 rupias
- 1 Euro equivale a 0,93 francos suizos
El programa pedirá por teclado la cantidad que queremos convertir y nos mostrará en pantalla los 
resultados con cuatro cifras decimales. De acuerdo a lo siguiente: si entramos la cantidad en euros 
nos convertirá a pesos, rupias y francos. Si entramos la cantidad en cualquier otra moneda nos dará 
solo el cambio en euros.
El programa reconocerá la moneda porque la cifra irá acompañada de una letra que indica la unidad: 
E para euros, P para pesos cubanos, R para rupias y F para francos suizos. Los cambios se harán 
siempre con cuatro cifras decimales máximo. 
A continuación dos ejemplos de ejecución:
 Introduce la cantidad: 25.755E 
25.75 euros equivalen a 719.3371 pesos cubanos, 2647.8716 rupias o 23.9522 francos suizos
 Introduce la cantidad: 1254,345R
 1254.345 rupias equivalen a 12.2006 euros
 NOTAS IMPORTANTES
 Los valores usados para el cambio deben de aparecer como variables en el programa para
facilitar modificaciones en el futuro. Además, debe de aparecer una única tasa de cambio 
por cada una de las monedas (no es válido tener el cambio de euro a peso cubano y además 
el de peso cubano a euro, por ejemplo ya que el segundo se puede sacar a partir del primero)
Suponemos que la entrada por teclado siempre es correcta, es decir, va a ser un número con
o sin decimales seguido de una letra (sin espacios entre ambos) que sólo puede ser la E, la P, 
la R o la F así que no tienes que hacer ningún tipo de validación"""

pesosCuba=27.93
rupias=102.81
francos=0.93

cantidad=input("Introduce la cantidad: ")

moneda=cantidad[-1:]
monedaMayus=moneda.upper()
monto=round(float(cantidad[:-1]),2)

match monedaMayus:
    case 'P':
        print(monto, " de Pesos Cubanos equivale a ", round((monto/pesosCuba),4), " euros")
    case 'R':
        print(monto, " de Rupias equivalen a ", round((monto/rupias),4), " euros")
    case 'F':
        print(monto," de Francos Suizos equivalen a ", round((monto/francos),4), " euros" )
    case 'E':
        print(monto, " equivalen a ", round((monto*pesosCuba),4), " Pesos Cubanos, ",
              round((monto*rupias),4)," Rupias o ",round((monto*francos),4), " Francos Suizos")