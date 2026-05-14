package ud11;

import java.sql.*;
import java.util.ArrayList;

public class Grupo {
    ArrayList <Alumno> alumnos;
    private String user="admin";
    private String pass="1234";
    private String uri="jdbc:mysql://localhost:3306/Grupo";
    public Grupo() {
        alumnos = new ArrayList<>();
        inicializarArrayList();
    }
    public void InsertaAlumno(Alumno alumno) {
        if (existeAlumno(alumno)) {
            System.out.println("El alumno ya existe por lo que no se puede insertar.");
        }
        else {
            try {
                Connection conexion = DriverManager.getConnection(uri,user,pass);
                Statement statement = conexion.createStatement();
                String introduccion = "INSERT INTO alumno (nombre,edad,calificacion) VALUES ('"+alumno.getNombre()+"',"+alumno.getEdad()+","+alumno.getNota()+")";
                System.out.println("Filas afectadas: "+ statement.executeUpdate(introduccion));
                alumnos.add(alumno);
            } catch (SQLException e) {
                System.out.println(e.getMessage());
            }
        }
    }
    public void inicializarArrayList() {
        try {
            Connection conexion = DriverManager.getConnection(uri,user,pass);
            Statement statement = conexion.createStatement();
            String consulta = "SELECT * FROM alumno";
            ResultSet rs = statement.executeQuery(consulta);
            boolean hayDatos = false;
                while (rs.next()) {
                    hayDatos = true;
                    String nombre = rs.getString("nombre");
                    int edad = rs.getInt("edad");
                    double calificacion = rs.getDouble("calificacion");
                    alumnos.add(new Alumno(nombre, edad, calificacion));
                }
            if (!hayDatos) {
                System.out.println("BBDD vacía!");
                }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        } catch (Excepcion e) {
            throw new RuntimeException(e);
        }
    }
    private boolean existeAlumno(Alumno alumno) {
        try {
            Connection conector = DriverManager.getConnection(uri,user,pass);
            Statement statement = conector.createStatement();
            String consulta = "SELECT * FROM alumno WHERE nombre ='"+alumno.getNombre()+"' AND edad = "+alumno.getEdad()+" AND calificacion = "+alumno.getNota();
            ResultSet rs = statement.executeQuery(consulta);
            if (rs.next()) {
                conector.close();
                return true;
            }
            conector.close();
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        return false;
    }
    public void Imprime() {
        String cad="";

        for (Alumno alumno : alumnos) {
            cad+= alumno;
        }
        System.out.print(cad);
    }
}
