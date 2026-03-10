package ud8;

public class Circulo extends Figuras {
    private double radio;
    private Punto centro;

    public Circulo(String nombre,double radio, Punto c){
        super(nombre);
        this.radio=radio;
        this.centro=c;
    }
    public double calcularArea(){
        double area=Math.PI*Math.pow(radio,2);
        return Math.round(area);
    }
    public double calcularVolumen(){
        return 0;
    }
    public double getRadio() {
        return radio;
    }
    public String toString() {
        return super.toString();
    }

}
