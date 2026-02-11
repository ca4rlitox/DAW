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

    public Fraccion sumaFraccion(Fraccion f2) {

        if (f2.getDenominador() == denominador) {
            return new Fraccion(f2.getNumerador()+numerador,denominador);
        }

        int d = ((f2.getNumerador()*denominador) + (f2.getDenominador()*numerador));
        int n = (denominador*f2.getDenominador());
        Fraccion rdso=new Fraccion(d,n);
        return rdso;
    }

    public Fraccion restaFraccion(Fraccion f2) {
        if (f2.getDenominador() != denominador) {
            return null;
        }

            int n = f2.getNumerador() - numerador;
            int d = f2.getDenominador();
            Fraccion rdso=new Fraccion(n,d);
        return rdso;
    }

    public Fraccion multiplicaFraccion(Fraccion f2) {
        int n = f2.getNumerador() * numerador;
        int d = f2.getDenominador() * denominador;
        Fraccion rdso=new Fraccion(n,d);
        return rdso;
    }

    public Fraccion divideFraccion(Fraccion f2) {
        int n = denominador * f2.getNumerador();
        int d = numerador * f2.getDenominador();
        Fraccion rdso=new Fraccion(n,d);
        return rdso;
    }

    public String toString() {
        return this.numerador+"/"+this.denominador;
    }
}
