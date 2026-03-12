package PracticaClinicaVeterinaria;

public class ClinicaVeterinaria {
    public static void main (String [] args) {
        Perro perro = new Perro("Marcos", "01/04/2004", 14.5, "PastorAleman", "38479382749DF39");
        perro.setComentarios("Es travieso");
        System.out.println(perro);
    }
}
