import mysql.connector


def buscarPelicula(nombrePelicula):
    try:
        conexion = mysql.connector.connect(host="localhost", user="admin", passwd="1234", database="sakila")
        cursor = conexion.cursor()
        cursor.execute(f"SELECT title FROM film WHERE title LIKE '{nombrePelicula}'")
        resultados = cursor.fetchall()
        if len(resultados) == 0:
            print(f"La película {nombrePelicula} no está en la base de datos")
            cursor.close()
            return False

        pelicula = "Pelicula: "
        for fila in resultados:
            pelicula+=fila[0]+":"

        print(pelicula)
        cursor.close()

        cursor = conexion.cursor()
        descripcion = "Descripcion: "
        cursor.execute(f"SELECT description FROM film WHERE title LIKE '{nombrePelicula}'")
        for fila in cursor:
            descripcion+=fila[0]

        print(descripcion)
        cursor.close()
        cursor = conexion.cursor()
        print("Reparto:")
        consulta_actores = f"""
                SELECT a.first_name, a.last_name 
                FROM actor a
                JOIN film_actor fa ON a.actor_id = fa.actor_id
                JOIN film f ON fa.film_id = f.film_id
                WHERE f.title LIKE '{nombrePelicula}'
            """
        cursor.execute(consulta_actores)
        for fila in cursor:
            print(f"{fila[1]}, {fila[0]}")

        cursor.close()
        conexion.close()
    except mysql.connector.Error as error:
        print(error)

buscarPelicula("ZORRO ARK")