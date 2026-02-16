package ud7;

public class Profesor extends Empleados {
    private String departamento;
    public Profesor (String nombre, String apellidos, String dni, String estadoCivil, String fechaIncorporacion, int numDespacho,
                     String departamento) {
        super(nombre, apellidos, dni, estadoCivil, fechaIncorporacion, numDespacho);
        this.departamento = departamento;
    }
    public String getDepartamento() {
        return departamento;
    }
    public void setDepartamento(String departamento) {
        this.departamento = departamento;
    }
    public String toString() {
        return super.toString()+" departamento: "+departamento;
    }
}
