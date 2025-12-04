package ud5;

import java.util.Scanner;

public class H6B2Ej3 {

    public static void main (String[] args) {
        // 3. Pedir al usuario una cadena y decir si empieza por el carácter ‘H’

        //Habilitamos escaner
        Scanner entrada = new Scanner(System.in);

        //Pedimos cadena
        System.out.println("Introduce una frase para saber si empieza por H");
        String cadena= entrada.nextLine();

        if (cadena.charAt(0) == 'H') {
            System.out.println("Tu cadena empieza por H.");
        }
        else {
            System.out.println("Tu cadena no empieza por H.");
        }

    }
}
