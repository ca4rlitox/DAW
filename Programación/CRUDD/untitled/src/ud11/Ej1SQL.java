package ud11;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

public class Ej1SQL {
    public static void main (String[] args) {
        Scanner entrada = new Scanner(System.in);
        String uri = "jdbc:mysql://localhost:3306/bd_clientes";
        String user = "admin";
        String pass = "1234";
        int opcion;

        try {
            //Paso 1: conexion a base de datos
            Connection connection = DriverManager.getConnection(uri, user, pass);
            System.out.println("Conectado a base de datos");
            //Paso 2: creamos un objeto que representa una instruccion SQL-DDL
            Statement statement = connection.createStatement();
            do {
                mostrarMenu();
                opcion = entrada.nextInt();
                switch (opcion) {
                    case 1:
                        System.out.println("Introduce el id: ");
                        int id = entrada.nextInt();
                        entrada.nextLine();
                        System.out.println("Introduce el nombre: ");
                        String nombre = entrada.nextLine();
                        System.out.println("Introduce la edad: ");
                        int age = entrada.nextInt();
                        String sql = "INSERT INTO clientes values ("+id+", '"+nombre+"', "+age+")";
                        int row = statement.executeUpdate(sql);
                        System.out.println("Se han modificado "+row+" filas");
                        break;
                    case 2:
                        System.out.println("Introduce el id: ");
                        id = entrada.nextInt();
                        entrada.nextLine();
                        System.out.println("Introduce el nuevo nombre: ");
                        nombre = entrada.nextLine();
                        System.out.println("Introduce la nueva edad: ");
                        age = entrada.nextInt();
                        sql = "UPDATE clientes SET edad=" + age + ", nombre='" + nombre + "' WHERE id=" + id;
                        row = statement.executeUpdate(sql);
                        System.out.println("Se han modificado "+row+" filas");
                        break;
                    case 3:
                        System.out.println("Introduce el id a borrar: ");
                        id = entrada.nextInt();
                        sql = "DELETE FROM clientes WHERE id="+id;
                        row = statement.executeUpdate(sql);
                        System.out.println("Se han modificado "+row+" filas");
                        entrada.nextInt();
                        break;
                    default:
                        System.out.println("Opcion inválida. Vuelve a intentarlo.");
                }

            } while(opcion !=4);

        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }

    }
    public static void mostrarMenu() {
        System.out.println("1. Para insertar");
        System.out.println("2. Para actualizar por id");
        System.out.println("3. Para borrar por id");
        System.out.println("4. Para salir");
    }
}
