package ud7;

//queremos que el dni se genere automaticamente
// y no se repita, iniciandose 1, 2, 3, etc...
public class Persona {
    private String nombre,apellidos,dni,estadoCivil;
    private static int idSiguiente=1; //Para que se vea dentro de todas las clases, static. Para que no sea visible desde fuera, private.

    public Persona(String nombre, String apellidos, String estadoCivil) {
        super();
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.dni = idSiguiente+"";
        this.estadoCivil = estadoCivil;
        idSiguiente++;
    }
    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getApellidos() {
        return apellidos;
    }
    public void setApellidos(String apellidos) {
        this.apellidos = apellidos;
    }
    public String getDni() {
        return dni;
    }
    public void setDni(String dni) {
        this.dni = dni;
    }
    public String getEstadoCivil() {
        return estadoCivil;
    }
    public void setEstadoCivil(String estadoCivil) {
        this.estadoCivil = estadoCivil;
    }
    public String toString() {
        return "Nombre: "+nombre+" Apellidos: "+apellidos+" Dni: "+dni+" Estado civil: "+estadoCivil;
    }
}
