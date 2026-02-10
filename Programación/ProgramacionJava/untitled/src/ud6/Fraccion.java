package ud6;

public class Fraccion {
    private int numerador;
    private int denominador;

    public Fraccion(int numerador, int denominador) {
    this.numerador = numerador;
    this.denominador = denominador;
    }
    public int getNumerador() {
        return numerador;
    }
    public int getDenominador() {
        return denominador;
    }
    public void setNumerador(int numerador) {
        this.numerador = numerador;
    }
    public void setDenominador(int denominador) {
        this.denominador = denominador;
    }

    public String sumaFraccion(Fraccion f2) {
        if (f2.getDenominador() != denominador) {
            return null;.0.................++++++0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        }
            int n = f2.getNumerador() + numerador;
            int d = f2.getDenominador();
            Fraccion rdso=new Fraccion(n,d);
        return rdso.toString();
    }

    public String restaFraccion(Fraccion f2) {
        if (f2.getDenominador() != denominador) {
            return null;
        }

            int n = f2.getNumerador() - numerador;
            int d = f2.getDenominador();
            Fraccion rdso=new Fraccion(n,d);
        return rdso.toString();
    }

    public String multiplicaFraccion(Fraccion f2) {
        int n = f2.getNumerador() * numerador;
        int d = f2.getDenominador() * denominador;
        Fraccion rdso=new Fraccion(n,d);
        return rdso.toString();
    }

    public String divideFraccion(Fraccion f2) {
        int n = f2.getNumerador() / denominador;
        int d = f2.getDenominador() / numerador;
        Fraccion rdso=new Fraccion(n,d);
        return rdso.toString();
    }

    public String toString() {
        return this.numerador+"/"+this.denominador;
    }
}
