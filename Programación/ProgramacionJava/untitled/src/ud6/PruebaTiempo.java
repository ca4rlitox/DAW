package ud6;

public class PruebaTiempo {

    public static void main (String[] args) {

        Tiempo t = new Tiempo(30,3,4);
        System.out.println(t.toString());

        t.setSegundos(9);
        t.setMinutos(4);
        t.setHora(10);

        System.out.println(t.toString());
    }


}
