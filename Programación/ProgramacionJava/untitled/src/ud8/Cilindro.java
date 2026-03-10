package ud8;

import static java.lang.Math.PI;
import static java.lang.Math.pow;

public class Cilindro extends Figuras {
    double altura;
    Circulo base;
    public Cilindro(String nombre,double radio, double altura){
        super(nombre);
       this.base=new Circulo(nombre,radio);
        this.altura = altura;
    }
    public double calcularArea(){
        double area=2*(PI*pow(base.getRadio(),2))+(2*PI*base.getRadio()*altura);
        return Math.round(area);
    }
    public double calcularVolumen(){
        double volumen= base.calcularArea()*altura;
        return  Math.round(volumen);
    }


    public String toString() {
        return super.toString();
    }
}
