package ud8;

public class Lavadora extends Electrodomestico {
    private double carga;
    final private int CARGA_FINAL=5;

    public Lavadora() {
        super();
        carga=CARGA_FINAL;
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
        return super.precioFinal();
    }
    public String toString() {
        return super.toString()+" carga: "+carga+" precio final lavadora: "+this.precioFinal();
    }

}
