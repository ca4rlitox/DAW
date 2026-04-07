package ud8.EjemploCasteoObj;

public class Persona {
    private String nombre;
    private int edad;
    public Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public int getEdad() {
        return edad;
    }

    public boolean equals (Object obj) {
        Persona p = (Persona) obj;
        //Importante castear, ya que está utilizando la clase objeto
        if (!(p instanceof Persona)) {
            return false;
        }

        return p.getNombre().equals(this.nombre) && p.getEdad() == this.edad;

    }

    public String toString() {
        return "Nombre: " + nombre + ", Edad: " + edad;
    }

}
