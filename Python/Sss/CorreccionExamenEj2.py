cambioPesos = 27.93
cambioFrancos = 0.93
entrada = input("Introduce la cantidad: ")
cantidad = float(entrada[:-1])
moneda = entrada[-1]

if moneda == 'P' or 'p':
    resultado = cantidad * cambioPesos
    print(cantidad,"pesos cubanos equivalen a", round(resultado,4),"euros")
elif moneda == 'F' or 'f':
    resultado = cantidad * cambioFrancos
    print(cantidad, "francos suizos equivalen a", round(resultado, 4), "euros")