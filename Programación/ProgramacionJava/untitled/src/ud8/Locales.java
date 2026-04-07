package ud8;

public class Locales extends Inmuebles {
    private int numVentanas;
    public Locales (String direccion, double m2, int numVentanas) {
        super(direccion,m2);
        this.numVentanas = numVentanas;
    }
    @Override
    public double precioFinal() {
        return 0;
    }
}
