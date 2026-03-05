package ud8;

public class PruebaElectrodomesticos {
    public static void main (String[] args) {
        Electrodomestico[] e = new Electrodomestico[10];
        Television tv = new Television();
        Lavadora lav = new Lavadora();
        double precioFinale=0;

        for (int i = 0; i < e.length; i++) {
            if (i<5) {
                e[i] = new Television();
            }
            else {
                e[i] = new Lavadora();
            }
        }
        for (int i = 0; i < e.length; i++) {
            precioFinale+= e[i].precioFinal();
        }
        System.out.println(precioFinale);




    }
}
