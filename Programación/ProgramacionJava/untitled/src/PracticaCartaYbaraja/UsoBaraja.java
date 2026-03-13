package PracticaCartaYbaraja;

public class UsoBaraja {
    public static void main (String[] args) {
        Carta carta = new Carta(10);

        System.out.println(carta.NombreCarta());
        System.out.println(carta.ValorMus(carta));
    }
}
