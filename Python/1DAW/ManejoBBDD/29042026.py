import mysql.connector

try:
    conexion = mysql.connector.connect(host="localhost", user="admin", passwd="1234", database="sakila")
    print("Conexion establecida")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM actor WHERE first_name LIKE 'RALPH' AND last_name LIKE 'CRUZ'") #Para ejecutar consultas
    for fila in cursor: #Asi se leen las consultas
        print(fila)
    #Como es una tupla, asi ponemos la columna que queremos sacar
        print(fila[2])
    tupla = cursor.fetchall()
    print(f"El select ha devuelto {len(tupla)} elementos")
    for linea in tupla:
        print(linea)
    cursor.close() #Cerramos cursor

    cursor = conexion.cursor()
    codigo = 16046
    hola = cursor.execute(f"DELETE FROM payment WHERE payment_id={codigo}")
    print(f"El comando ha afectado a {cursor.rowcount} elementos")

    conexion.commit() #Guardamos cambios con el commit
    conexion.close() #Cerramos conexion
except mysql.connector.Error as error: #Para añadir una excepcion concreta, como el IOException de Java
    print(error)