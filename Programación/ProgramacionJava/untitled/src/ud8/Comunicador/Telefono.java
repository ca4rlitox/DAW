package ud8.Comunicador;

public abstract class Telefono {
    private String marca,tfn;

    public Telefono(String marca, String tfn) {
        this.marca = marca;
        this.tfn = tfn;
    }
    public String getMarca() {
        return marca;
    }
    public String getTfn() {
        return tfn;
    }
    public void setTfn(String tfn) {
        this.tfn = tfn;
    }

    public abstract String toString();
}
