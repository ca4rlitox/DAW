package ud5;

import java.util.Scanner;

public class H6B2Ej8 {

    public static void main (String[] args) {
        // 8. Repite el ejercicio anterior pero usando indexOf

        //Habilitamos escaner
        Scanner entrada = new Scanner(System.in);

        //Pedimos frase
        System.out.println("Introduce una frase: ");
        String cadena = entrada.nextLine();

        //Pedimos que caracter quiere buscar
        System.out.println("¿Qué caracter quieres buscar su posición?");
        char caracterAbuscar = entrada.nextLine().charAt(0);

        System.out.println("El caracter "+caracterAbuscar+" está en la posicion "+cadena.indexOf(caracterAbuscar));

    }
}
