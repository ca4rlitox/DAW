package ud7;

public class PersonaldeServicio extends Empleados {
    private String seccion;
    public PersonaldeServicio (String nombre, String apellidos, String dni, String estadoCivil, String fechaIncorporacion, int numDespacho, String seccion) {
        super(nombre, apellidos, dni, estadoCivil, fechaIncorporacion, numDespacho);
        this.seccion = nombre;
    }
    public  String getSeccion() {
        return seccion;
    }
    public void setSeccion(String seccion) {
        this.seccion = seccion;
    }
    public String toString() {
        return super.toString()+" seccion: "+seccion;
    }
}
