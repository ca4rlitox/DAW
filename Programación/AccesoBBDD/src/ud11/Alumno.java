package ud11;

public class Alumno {
    private String nombre;
    int edad;
    double nota;

    public Alumno(String nombre, int edad, double nota) throws Excepcion {
        setNombre(nombre);
        setEdad(edad);
        setNota(nota);
    }

    public String getNombre() {
        return nombre;
    }

    public double getNota() {
        return nota;
    }

    public int getEdad() {
        return edad;
    }

    public void setNombre(String nombre) throws Excepcion {
        if (!nombre.isEmpty()) {
            this.nombre = nombre;
        }
        else {
            throw new Excepcion("No puede estar el nombre vacío.");
        }
    }
    public void setEdad (int edad) throws Excepcion {
        if (edad >= 18 && edad < 100) {
            this.edad = edad;
        }
        else {
            throw new Excepcion("La edad debe estar comprendida entre 18 y 100.");
        }
    }
    public void setNota(double calificacion) throws Excepcion {
        if (calificacion >= 0 && calificacion <= 10) {
            this.nota = calificacion;
        }
        else {
            throw new Excepcion("La nota debe estar comprendida entre 18 y 100.");
        }
    }
    public String toString() {
        return "Nombre: "+getNombre()+", edad: "+getEdad()+", calificacion: "+getNota()+"\n";
    }
}
