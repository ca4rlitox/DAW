package ud5;

import java.util.Scanner;

public class H6B2Ej6 {
    public static void main(String[] args) {

        //6. Elabora un programa que escriba todos los caracteres de una cadena cada uno en una línea.

        //Habilitamos escaner
        Scanner entrada = new Scanner(System.in);
        //Habilitamos variable
        char caracter;

        System.out.println("Introduce cadena de caracteres");
        String cadena = entrada.nextLine();

        for (int i = 0;i<=cadena.length()-1;i++) {
            caracter = cadena.charAt(i);
            System.out.println(caracter);
        }
    }
}
