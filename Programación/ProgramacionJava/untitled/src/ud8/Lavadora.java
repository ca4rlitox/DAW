package ud8;

public class Lavadora extends Electrodomestico {
    private double carga;
    finaprivate int CARGA_FINAL =
    public Lavadora() {
        super();
        carga=5;
    }
    public Lavadora(double precio, double peso) {
        super(precio, peso);
    }
    public Lavadora(double carga) {
        super();
        this.carga=carga;
    }
    public double getCarga() {
        return carga;
    }
    public double precioFinal() {
        if (carga >= 30) return super.precioFinal()+50;
        return super.precioFinal()+50;
        }
}
