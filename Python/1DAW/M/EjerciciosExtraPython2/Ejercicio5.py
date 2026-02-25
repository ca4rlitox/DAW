from datetime import datetime, timedelta

reservas = [
    {"habitacion": 101, "cliente": "García", "entrada": "15/03/2025", "salida": "20/03/2025"},
    {"habitacion": 102, "cliente": "López", "entrada": "10/04/2025", "salida": "15/04/2025"},
]

def duracion_estancia(entrada_str,salida_str):
    try:
        entrada_obj=datetime.strptime(entrada_str,"%d/%m/%Y")
        salida_obj=datetime.strptime(salida_str,"%d/%m/%Y")
        #dias_salida=int(datetime.strftime(salida_obj,"%d"))
        #dias_entrada=int(datetime.strftime(entrada_obj,"%d"))
        #return dias_salida - dias_entrada
        return (salida_obj - entrada_obj).days
    except:
        return None

def mostrar_reservas():
    print("RESERVAS DEL HOTEL:")
    print("====================")
    for reserva in reservas:

        print(f"""Habitación: {reserva['habitacion']} - {reserva['cliente']}
Entrada: {reserva['entrada']} | Salida: {reserva['salida']}
Duración: {duracion_estancia(reserva['entrada'],reserva['salida'])} noches
""")

def nueva_reserva(hab,cliente,entrada_str,salida_str):
    try:
        entrada_obj=datetime.strptime(entrada_str,"%d/%m/%Y")
        salida_obj=datetime.strptime(salida_str,"%d/%m/%Y")
        if entrada_obj < salida_obj:
            reservas.append({'habitacion':hab, 'cliente':cliente, 'entrada':entrada_str, 'salida':salida_str})
        else:
            print("La reserva no es válida")
    except ValueError:
        print("Fecha incorrecta")


nueva_reserva(103,"Gimenez","06/09/2025","12/09/2025")
nueva_reserva(103,"Gimenez","06/09/2025","03/09/2025")
nueva_reserva(104,"Rey","32/13/2025","12/12/2025")
mostrar_reservas()