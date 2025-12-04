package ud5;

import java.util.Scanner;

public class H6B2Ej1 {

    public static void main (String[] args) {
        /*1. Pedir al usuario su nombre y saludarlo.*/
        //Habilitamos escaner
        Scanner entrada = new Scanner(System.in);

        //Pedimos nombre
        System.out.println("Introduce tu nombre");
        String nombre = entrada.nextLine();
        //Saludamos
        System.out.println("Hola "+nombre+"!");


    }

}
