package ud7bis;

public class EmpleadoPorComision extends Empleado{
    private int ventas;
    private double comision;
    public EmpleadoPorComision(String nombre, String apellido, int numSS, double salario) {
        super(nombre, apellido, numSS, setSalario(ventas*comision));
        this.ventas=0;
        this.comision=0;
    }
    public void setSalario(int ventas, double comision){
        setSalario(ventas*comision);
    }

}
