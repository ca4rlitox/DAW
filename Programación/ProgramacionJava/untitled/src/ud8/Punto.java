package ud8;

public class Punto extends Figuras {
    private int x,y;

    public Punto(String nombre, int x, int y) {
        super(nombre);
        this.x = x;
        this.y = y;
    }
    public double calcularArea(){
        return 0;
    }
    public double calcularVolumen(){
        return 0;
    }
    public String toString(){
        return super.toString();
    }
}
