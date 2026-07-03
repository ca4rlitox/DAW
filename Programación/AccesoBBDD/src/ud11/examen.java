package ud11;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

public class examen {
    public static void main (String [] args) {
        String uri = "jdbc:mysql://localhost:3306/escuela";
        String user = "admin";
        String pass = "1234";
        Scanner entrada = new Scanner(System.in);
        int opcion;

        try {
            Connection conector = DriverManager.getConnection(uri,user,pass);
            do {
                System.out.println("menu");
                opcion= entrada.nextInt();
                switch (opcion) {
                    case 1:
                        System.out.println("Introduce el id:");
                        int id = entrada.nextInt();
                        entrada.nextLine();
                        if (opcion == 1) {
                            System.out.println("Introduce el nombre:");
                            String nombre = entrada.nextLine();
                            System.out.println("Introduce la nota");
                            double nota = entrada.nextDouble();
                            if (nota < 0 && nota > 10) {
                                do {
                                    System.out.println("Introduce nota entre 0 y 10");
                                    nota = entrada.nextDouble();
                                } while (nota < 0 && nota > 10);
                            }
                            Statement statement = conector.createStatement();
                            String consulta = "INSERT INTO notas VALUES ("+id+",'"+nombre+"',"+nota+")";
                            int row = statement.executeUpdate(consulta);
                            if (row == 1) {
                                System.out.println("Se ha introducido de manera correcta.");
                            } else {
                                System.out.println("No se ha introducido.");
                            }
                            statement.close();
                        } else {
                            System.out.println("No se ha introducido ya que ya existe.");
                        }
                        break;
                    case 2:
                        System.out.println("Introduce el id a borrar: ");
                        id = entrada.nextInt();
                        Statement stmt = conector.createStatement();

                        break;
                }
            } while (opcion != 4);

        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }
}
