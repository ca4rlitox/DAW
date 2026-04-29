package ud11;

public class Alumno {
    private String nombre;
    private int calificacion,edad;

    public Alumno (String nombre, int calificacion, int edad) {
        setNombre(nombre);
        setCalificacion(calificacion);
        setEdad(edad);
    }
    public String getNombre() {
        return nombre;
    }
    public int getCalificacion() {
        return calificacion;
    }
    public int getEdad() {
        return edad;
    }
    public void setNombre(String nombre) {
        if (nombre.isEmpty()) {
            System.out.println("No se puede inicializar el nombre en blanco.");
        }
        else {
            this.nombre = nombre;
        }
    }
    public void setCalificacion(int calificacion) {
        if (calificacion >= 0 && calificacion <= 10) {
            this.calificacion = calificacion;
        }
    }
    public void setEdad(int edad) {
        if (edad >= 18 && edad <=100) {
            this.edad = edad;
        }
    }
    public String toString() {
        return "Nombre: "+this.nombre+" edad: "+this.edad+" calificación: "+this.calificacion;
    }
}
