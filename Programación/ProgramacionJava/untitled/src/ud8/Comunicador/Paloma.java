package ud8.Comunicador;

public abstract class Paloma extends Ave {
    private String color;
    private char sexo;

    public Paloma(boolean vuela, String especie, String color, char sexo) {
        super(vuela, especie);
        this.color = color;
        this.sexo = sexo;
    }
}
