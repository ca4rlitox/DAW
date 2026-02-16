package ud7;

public class Coche extends Vehiculo {
    private int CV;

    public Coche(int ruedas, String color, String matricula, int CV) {
        super(true,4,color,matricula);
        this.CV = CV;
    }
    public int getCV() {
        return CV;
    }
    public void setCV(int CV) {
        this.CV = CV;
    }

    public String toString() {
        return super.toString()+" CV: "+this.CV;
    }
}
