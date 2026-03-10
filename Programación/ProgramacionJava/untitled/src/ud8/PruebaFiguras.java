package ud8;

import java.util.ArrayList;

public class PruebaFiguras {
    public static void main(String[] args) {
        ArrayList<Figuras> figuras = new ArrayList<Figuras>();
        figuras.add(new Punto("Punto1"));
        figuras.add(new Circulo("Circulo1",1.5));
        figuras.add(new Cilindro("Cilindro1",1.5,2.5));

        for (Figuras figura : figuras) {
            System.out.println(figura);
        }
    }
}
