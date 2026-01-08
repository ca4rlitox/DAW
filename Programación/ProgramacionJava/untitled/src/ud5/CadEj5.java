package ud5;

import java.util.Scanner;

public class CadEj5 {
    public static void main (String[] args) {

        Scanner entrada = new Scanner(System.in);
        String cad="";

        System.out.println("Introduce un caracter: ");
        char caracter = entrada.nextLine().charAt(0);
        System.out.println("Introduce cuantas veces quieres que se repita: ");
        int numVeces = entrada.nextInt();

        for (int i = 0; i < numVeces; i++) {

            cad+=caracter;

        }

        System.out.println(cad);



    }
}
