package ud11;


import java.sql.*;

public class insertarBD {
    public static void main (String[] args) {
        //Paso 1. Conectar con el SGBD
        String user="admin";
        String pass="1234";
        String uri="jdbc:mysql://localhost:3306/BD_CLIENTES";
        String consulta="INSERT INTO clientes VALUES ('1323a','Paco',40)";

        try (Connection conector = DriverManager.getConnection(uri, user, pass)) /* Creamos la conexion */ {
            Statement statement = conector.createStatement(); /*Creamos un objeto que simboliza una instruccion SQL*/
            int rows = statement.executeUpdate(consulta); /* Ejecutamos la instruccion SQL */
            System.out.println("Filas afectadas: "+rows);
            // El select devuelve un resultset para escribir
            conector.close();


        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }

    }
}
