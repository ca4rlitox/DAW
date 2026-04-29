package ud11;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class Grupo {
    private ArrayList<Alumno> alumnos;
    public Grupo() {
        alumnos = new ArrayList<>();
    }
    public boolean InsertaAlumnoLista(Alumno alumno) {
        if (alumnos.contains(alumno)) return false;

        alumnos.add(new Alumno(alumno.getNombre(), alumno.getCalificacion(), alumno.getEdad()));
        return true;
    }
    public void Imprime() {
        for (Alumno alumno : alumnos) {
            System.out.println(alumno);
        }
    }
    public void EscribeFicheroAlumnos() {
        int numAlumnos= alumnos.size();
        try (FileWriter escritura = new FileWriter("alumnos.txt")) {
            escritura.write(numAlumnos+"\n");
            for (Alumno alumno : alumnos) {
                escritura.write(alumno.getNombre()+"--"+alumno.getEdad()+"--"+alumno.getCalificacion()+"\n");
            }
            escritura.close();
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
    public void LeeFicheroAlumnos(String nomFich) {
        String cadena="";
        int caracter='A';
        try (FileReader lectura = new FileReader(nomFich)) {
            int numAlumno = lectura.read();
            cadena+=((char)numAlumno)+"\n";
            while ((caracter = lectura.read()) != -1) {
                    cadena+=(char) caracter;
            }
            lectura.close();
        } catch(IOException e) {
            System.out.println(e.getMessage());
        }
        System.out.print(cadena);
    }
}
