package ud11;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class EjemploInsercion {
    public static void main (String[] args) {
        String uri = "jdbc:mysql://localhost:3306/bd_clientes";
        String user = "admin";
        String pass = "1234";
        //Paso 1: conexion a base de datos
        try {
            Connection connection = DriverManager.getConnection(uri, user, pass);
            System.out.println("Conectado a base de datos");
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }
}
