package ud7bis;

public class EmpleadoBaseMasComision extends Empleado {
    private int ventas;
    private double comision;

    public EmpleadoBaseMasComision(String nombre, String apellido, String numSS, int ventas,  double comision) {
        super(nombre, apellido, numSS, 0);
        this.ventas = ventas;
        this.comision = comision;
    }

    public int getVentas() {
        return ventas;
    }
    public void setVentas(int ventas) {
        this.ventas = ventas;
    }
    public double getComision() {
        return comision;
    }
    public void setComision(double comision) {
        this.comision = comision;
    }
    public double  calcularSalario() {
        return this.getSalarioBase()+(ventas * comision);
    }

}
