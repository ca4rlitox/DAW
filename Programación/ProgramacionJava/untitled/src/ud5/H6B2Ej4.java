package ud5;

import java.util.Scanner;

public class H6B2Ej4 {
    public static void main (String[] args) {
        // 4. Como el anterior, pero sin importar si es mayúscula o minúscula.

        //Habilitamos escaner
        Scanner entrada = new Scanner(System.in);

        //Pedimos cadena
        System.out.println("Introduce una frase para saber si empieza por H/h");
        String cadena= entrada.nextLine();

        if ((cadena.charAt(0) == 'h') || (cadena.charAt(0) == 'H')) {
            System.out.println("Tu cadena empieza por h.");
        }
        else {
            System.out.println("Tu cadena no empieza por h.");
        }



    }
}
