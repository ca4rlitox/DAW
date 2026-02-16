package ud7;

public class Vehiculo {
    private boolean tieneMotor;
    private int ruedas;
    private String color;
    private String matricula;

    public Vehiculo (boolean tieneMotor, int ruedas, String color, String matricula) {
        super();
        this.tieneMotor = tieneMotor;
        this.ruedas = ruedas;
        this.color = color;
        this.matricula = matricula;
    }

    public void setTieneMotor(boolean tieneMotor) {
        this.tieneMotor = tieneMotor;
    }
    public void setRuedas(int ruedas) {
        this.ruedas = ruedas;
    }
    public void setColor(String color) {
        this.color = color;
    }
    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }
    public boolean getTieneMotor() {
        return tieneMotor;
    }
    public int getRuedas() {
        return ruedas;
    }
    public String getColor() {
        return color;
    }
    public String getMatricula() {
        return matricula;
    }
    public String toString() {
        return "Tiene motor: "+tieneMotor+", ruedas: "+ruedas+", color: "+color+", matricula: "+matricula;
    }
}
