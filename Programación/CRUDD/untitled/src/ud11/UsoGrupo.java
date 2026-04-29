package ud11;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Scanner;

public class UsoGrupo {
    public static void main (String[] args) {
        Grupo grupo = new Grupo();
        Scanner entrada = new Scanner(System.in);
        String uri = "jdbc:mysql://localhost:3306/bd_clientes";
        String user = "admin";
        String pass = "1234";
        int opcion;

        try (Connection connection = DriverManager.getConnection(uri, user, pass)) {

        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }

    }
}
