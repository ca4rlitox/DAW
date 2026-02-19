package ud6;

public class Raices {
    private double a, b, c;

    public Raices(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }
    public double getA() {
        return a;
    }
    public void setA(double a) {
        this.a = a;
    }
    public double getB() {
        return b;
    }
    public void setB(double b) {
        this.b = b;
    }
    public double getC() {
        return c;
    }
    public void setC(double c) {
        this.c = c;
    }
    public double getDiscriminante() {
        return (b*b)-(4*a*c);
    }
    public boolean tieneRaiz() {
        return getDiscriminante() >= 0;
    }
    public boolean tieneRaices() {
        return getDiscriminante() > 0;
    }
    public void calcular() {
        double discriminante = getDiscriminante();
        double raiz1,raiz2;
        if (discriminante == 0) {
            raiz1 = ((-1*b)/(2*a));
            System.out.println("La única solución es: "+raiz1);
        }
        else if (discriminante < 0) {
            System.out.println("La raíz no tiene solución");
        }
        else {
            raiz1=(-(b)+Math.sqrt(discriminante));
            raiz1=raiz1/(2*a);
            System.out.println("El valor de la primera solución es: "+raiz1);
            raiz2=(-(b)-Math.sqrt(discriminante));
            raiz2=raiz2/(2*a);
            System.out.println("El valor de la segunda solución es: "+raiz2);
        }
    }
    public void obtenerRaiz() {
        calcular();
    }
    public void obtenerRaices() {
        calcular();
    }
}
