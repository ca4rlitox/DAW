package ud8;

public class Pisos extends Inmuebles {
    private String numPiso;
    public Pisos (String direccion, double m2, String numPiso) {
        super(direccion,m2);
        this.numPiso = numPiso;
    }

    @Override
    public double precioFinal() {
        return 0;
    }
}
