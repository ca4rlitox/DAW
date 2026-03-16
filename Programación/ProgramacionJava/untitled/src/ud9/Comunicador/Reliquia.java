package ud9.Comunicador;

public abstract class Reliquia {
    private int ano;

    public Reliquia(int ano) {
        this.ano = ano;
    }

    public int getAno() {
        return ano;
    }

    public abstract String toString();
}
