package ud11;


import java.sql.*;

public class insertarBD {
    public static void main (String[] args) {
        //Paso 1. Conectar con el SGBD
        String user="admin";
        String pass="1234";
        String uri="jdbc:mysql://localhost:3306/BD_CLIENTES";
        String consulta="SELECT * FROM clientes";

        try (Connection conector = DriverManager.getConnection(uri, user, pass)) /* Creamos la conexion */ {
            Statement stmt = conector.createStatement(); /*Creamos un objeto que simboliza una instruccion SQL*/
            ResultSet consultas = stmt.executeQuery(consulta);
            System.out.println("Conexion OK");
            System.out.println(consultas);

        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }

    }
}
