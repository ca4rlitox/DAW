package ud5;

import java.util.Scanner;

public class H6B2Ej9 {
    public static void main (String[] args) {

        //9. Programa que reciba como entrada una cadena y un carácter y escriba cuántas veces aparece
        // ese carácter en la cadena. No se puede usar indexOf.

        //Habilitamos escaner
        Scanner entrada = new Scanner(System.in);
        //Habilitamos variable contar
        int recuento=0;

        //Pedimos frase
        System.out.println("Introduce una frase: ");
        String cadena = entrada.nextLine();

        //Pedimos que caracter quiere buscar
        System.out.println("¿Qué caracter quieres contar?");
        char caracterAcontar = entrada.nextLine().charAt(0);

        //Hacemos bucle para ver en que posicion está sin usar indexOf

        for (int i = 0;i<=cadena.length() - 1;i++) {
        if (caracterAcontar == cadena.charAt(i)) {
            recuento++;
        }
        else {
            recuento=recuento;
        }
        }
        System.out.println("El recuento del caracter "+caracterAcontar+" es de "+recuento+".");


    }
}
