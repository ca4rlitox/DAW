package ud5;

import java.util.Scanner;

public class H6B2Ej2 {
    public static void main (String[] args) {

        //2. Programa que diga si una cadena dada por el usuario está o no vacía

        //Habilitamos escaner
        Scanner entrada = new Scanner(System.in);
        //Pedimos cadena
        System.out.println("Introduce una frase: ");
        String cadena = entrada.nextLine();

        if (cadena.isEmpty()) {
            System.out.println("Cadena vacia.");
        }
        else {
            System.out.println("Cadena no vacía.");
        }


    }
}
