package ud8;

public abstract class Inmuebles {
    private String direccion;
    private double m2;
    public Inmuebles (String direccion, double m2) {
        this.direccion = direccion;
        this.m2 = m2;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    public double getM2() {
        return m2;
    }

    public void setM2(double m2) {
        this.m2 = m2;
    }

    public abstract double precioFinal();
}
