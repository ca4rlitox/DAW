package ud11;

import java.sql.*;
import java.util.Scanner;

public class menuBD {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        String user = "admin";
        String pass = "1234";
        String uri = "jdbc:mysql://localhost:3306/BD_CLIENTES";
        int opcion;

        try {
            //Creamos la conexión SQL
            Connection conector = DriverManager.getConnection(uri, user, pass);
            do {
                mostrarMenu();
                opcion = entrada.nextInt();
                switch (opcion) {
                    case 1:
                        entrada.nextLine();
                        System.out.println("Introduce el id del cliente");
                        String id = entrada.nextLine();
                        System.out.println("Introduce el nombre");
                        String nombre = entrada.nextLine();
                        System.out.println("Introduce la edad.");
                        int edad = entrada.nextInt();
                        Statement statement = conector.createStatement(); //Creamos la instruccion
                        String consulta = "INSERT INTO clientes values ('" + id + "','" + nombre + "'," + edad + ")";
                        System.out.println("Filas afectadas: "+ statement.executeUpdate(consulta));
                        break;
                    case 2:
                        entrada.nextLine();
                        System.out.println("Introduce el id a actualizar");
                        id = entrada.nextLine();
                        System.out.println("Introduce el nuevo nombre: ");
                        nombre = entrada.nextLine();
                        System.out.println("Introduce la nueva edad: ");
                        edad = entrada.nextInt();
                        consulta = "UPDATE clientes SET nombre = '"+nombre+"', edad = "+edad+" WHERE id = '"+id+"'";
                        Statement stmt = conector.createStatement(); //Creamos la instruccion
                        System.out.println("Filas afectadas: "+stmt.executeUpdate(consulta));
                        break;
                    case 3:
                        entrada.nextLine();
                        System.out.println("Introduce el id a borrar");
                        id = entrada.nextLine();
                        consulta = "DELETE from clientes WHERE id = '"+id+"'";
                        Statement stamt = conector.createStatement();
                        System.out.println("Filas afectadas: "+stamt.executeUpdate(consulta));
                        break;
                    case 4:
                        entrada.nextLine();
                        System.out.println("Introduce el id a revisar: ");
                        nombre = entrada.nextLine();
                        Statement statement1 = conector.createStatement();
                        consulta = "SELECT * FROM clientes WHERE id = "+nombre;
                        ResultSet rs = statement1.executeQuery(consulta);
                        while(rs.next()) {
                            id = rs.getString("id");
                            nombre = rs.getString("nombre");
                            edad = rs.getInt("edad");
                            System.out.println("ID: "+id+" nombre: "+nombre+" edad: "+edad);
                        }
                        break;
                    case 5:
                        entrada.nextLine();
                        Statement statement2 = conector.createStatement();
                        consulta = "SELECT * FROM clientes";
                        ResultSet rs1 = statement2.executeQuery(consulta);
                        while (rs1.next()) {
                            id = rs1.getString("id");
                            nombre = rs1.getString("nombre");
                            edad = rs1.getInt("edad");
                            System.out.println("ID: "+id+" nombre: "+nombre+" edad: "+edad);
                        }
                        break;
                    case 6:
                        System.out.println("Has salido correctamente.");
                        break;
                    default:
                        System.out.println("Opción no válida. Intentalo de nuevo.");
                }

            } while (opcion != 6);
            conector.close();

    } catch(SQLException e) {
        System.out.println(e.getMessage());
    }
}
    public static void mostrarMenu() {
        System.out.println("1. Insertar cliente");
        System.out.println("2. Actualizar por id");
        System.out.println("3. Borrar por id");
        System.out.println("4. Consultar por id");
        System.out.println("5. Consultar todos los datos en la BBDD");
        System.out.println("6. Salir");
    }
    }