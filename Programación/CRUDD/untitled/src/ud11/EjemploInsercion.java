package ud11;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class EjemploInsercion {

        public static void main (String[] args) {
            String uri = "jdbc:mysql://localhost:3306/bd_clientes";
            String user = "admin";
            String pass = "1234";

            try {
                //Paso 1: conexion a base de datos
                Connection connection = DriverManager.getConnection(uri, user, pass);
                System.out.println("Conectado a base de datos");
                //Paso 2: creamos un objeto que representa una instruccion SQL-DDL
                Statement statement = connection.createStatement();
                //Paso 3: Ejecutamos la sentencia SQL
                    String sql = "INSERT INTO clientes values (3,'Paco',11)";
                    int row = statement.executeUpdate(sql);
                    System.out.println("Se han afectado "+row+" filas");

                //ExecuteUpdate ejecuta instrucciones INSERT, UPDATE, DELETE

            } catch (SQLException e) {
                System.out.println(e.getMessage());
            }
        }
    }