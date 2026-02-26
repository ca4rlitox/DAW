package ud7bis;

public class Empleado {
    private String nombre,apellido,numSS;
    private double salarioBase;

    public Empleado(String nombre, String apellido, String numSS, double salarioBase) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.numSS = numSS;
        this.salarioBase = salarioBase;
    }
    public String getNumSS() {
        return numSS;
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
    public double getSalarioBase() {
        return salarioBase;
    }
    public void setSalarioBase(double salarioBase) {
        this.salarioBase = salarioBase;
    }

    public String toString() {
        return "Nombre: "+nombre+" apellido: "+apellido+" num seguridad social: "+numSS+" salario: "+ salarioBase;
    }
}
