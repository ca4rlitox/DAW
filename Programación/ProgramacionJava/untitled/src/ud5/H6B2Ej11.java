package ud5;

import java.util.Scanner;

public class H6B2Ej11 {
    public static void main (String[] args) {
        // 11. Programa que lea una frase carácter a carácter hasta que reciba ‘#’ y lo guarde todo en una
        //cadena.

        //Habilitamos escaner y variables
        Scanner entrada = new Scanner(System.in);
        char caracter=' ';
        String cadena="";

        //Pedimos caracteres
        System.out.println("Escribe caracteres para concatenarlos en una cadena, y cuando quieras parar, pon #");
        //Solicitamos caracteres y hacemos bucle do while
        do {
            caracter = entrada.nextLine().charAt(0);
            if (caracter!='#'){
                cadena += caracter;
            }
        } while (caracter!='#');
        System.out.println(cadena);
    }
}
