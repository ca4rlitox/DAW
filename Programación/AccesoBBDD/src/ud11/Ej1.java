package ud11;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

public class Ej1 {
    public static void main (String[] args) throws Excepcion {
        Scanner entrada = new Scanner(System.in);
        String user = "admin";
        String pass = "1234";
        String uri = "jdbc:mysql://localhost:3306/BD_CLIENTES";

        Grupo grupo = new Grupo();
        grupo.Imprime();
        grupo.InsertaAlumno(new Alumno("Pepe",20,8));
        grupo.InsertaAlumno(new Alumno("Gonzalo",58,6));
        grupo.Imprime();
    }
}
