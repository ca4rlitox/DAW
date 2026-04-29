import mysql.connector

try:
    conexion = mysql.connector.connect(host="localhost", user="admin", passwd="1234", database="sakila")
    print("Conexion establecida")




    conexion.commit()
    conexion.close()
except mysql.connector.Error as error: #Para añadir una excepcion concreta, como el IOException de Java
    print(error)