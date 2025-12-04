package ud5;

import java.util.Scanner;

public class H6B2Ej7 {
    public static void main (String[] args) {
        //Pedir al usuario una frase y un carácter, y decir en qué posiciones está ese carácter, o indicar
        //que no está si procede. No se puede usar indexOf o similar.

        //Habilitamos escaner
        Scanner entrada = new Scanner(System.in);

        //Pedimos frase
        System.out.println("Introduce una frase: ");
        String cadena = entrada.nextLine();

        //Pedimos que caracter quiere buscar
        System.out.println("¿Qué caracter quieres buscar su posición?");
        char caracterAbuscar = entrada.nextLine().charAt(0);

        //Hacemos bucle para ver en que posicion está sin usar indexOf

        for (int i = 0;i<=cadena.length() - 1;i++) {
            if (caracterAbuscar == cadena.charAt(i)) {
                System.out.println("El caracter que estás buscando esta en la posición: "+i);
            }
        }



    }
}
