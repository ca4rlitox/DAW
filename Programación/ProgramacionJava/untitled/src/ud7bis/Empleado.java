package ud7bis;

public class Empleado {
    private String nombre;
    private String apellido;
    private int numSS;
    private double salario;

    public Empleado(String nombre, String apellido, int numSS, double salario) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.numSS = numSS;
        this.salario = salario;
    }
    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getApellido() {
        return apellido;
    }
    public void setApellido(String apellido) {
        this.apellido = apellido;
    }
    public int getNumSS() {
        return numSS;
    }
    public void setNumSS(int numSS) {
        this.numSS = numSS;
    }
    public double getSalario() {
        return salario;
    }
    public void setSalario(double salario) {
        this.salario = salario;
    }

    public String toString() {
        return "Nombre: "+nombre+" apellido: "+apellido+" num seguridad social: "+numSS+" salario: "+salario;
    }
}
