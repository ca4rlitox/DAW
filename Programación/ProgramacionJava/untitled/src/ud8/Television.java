package ud8;

public class Television extends Electrodomestico{
    private int resolucion;
    private boolean sintonizadorTDT;

    public Television(){
        super();
        this.sintonizadorTDT = false;
        this.resolucion=20;
    }
    public Television(double precioBase, double peso) {
        this();
        setPrecioBase(precioBase);
        setPeso(peso);
    }

    public Television(String color, char consumoEnergetico, double precioBase, double peso, boolean sintonizadorTDT, int resolucion) {
        super(color, consumoEnergetico, precioBase, peso);
        this.sintonizadorTDT = sintonizadorTDT;
        this.resolucion = resolucion;
    }
    public double precioFinal() {
        if (this.resolucion > 40 && sintonizadorTDT) return super.precioFinal()*1.30+50;
        if (this.resolucion > 40) return super.precioFinal()*1.30;
        if (sintonizadorTDT) return super.precioFinal()+50;
        return super.precioFinal();
    }
    public String toString() {
        return super.toString()+" precio final: "+this.precioFinal()+" resolucion: "+this.resolucion+" sintonizador: "+sintonizadorTDT;
    }
}
