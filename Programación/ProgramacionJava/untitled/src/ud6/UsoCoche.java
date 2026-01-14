package ud6;

public class UsoCoche {

    public static void main (String[] args) {
    //Construyo un objeto de tipo coche
    Coche seat = new Coche();
    seat.matricula="6097GRZ";
    seat.color="blanco";
    seat.motor="125cv";

    seat.arrancar();
    seat.pitar();
        System.out.println(seat.dameRuedas());

}
}
