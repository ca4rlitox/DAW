package ud7;

public class Empleados extends Persona {
    private String fechaIncorporacion;
    private int numDespacho;

    public Empleados(String nombre, String apellidos, String dni, String estadoCivil, String fechaIncorporacion, int numDespacho) {
        super(nombre, apellidos, dni, estadoCivil);
        this.fechaIncorporacion = fechaIncorporacion;
        this.numDespacho = numDespacho;
    }
    public String getFechaIncorporacion() {
        return fechaIncorporacion;
    }
    public void setFechaIncorporacion(String fechaIncorporacion) {
        this.fechaIncorporacion = fechaIncorporacion;
    }
    public int getNumDespacho() {
        return numDespacho;
    }
    public void setNumDespacho(int numDespacho) {
        this.numDespacho = numDespacho;
    }
    public String toString() {
        return super.toString()+" Fecha incorporacion: "+fechaIncorporacion+" Despacho "+numDespacho;
    }
}
