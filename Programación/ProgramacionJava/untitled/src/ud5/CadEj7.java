package ud5;

import java.util.Scanner;

public class CadEj7 {
    public static void main (String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.println("Introduce una cadena: ");
        String cad = entrada.nextLine();
        System.out.println("Introduce el caracter que quieres buscar: ");
        char caracter = entrada.nextLine().charAt(0);

        for (int i = 0; i < cad.length(); i++) {
            char caracterActual = cad.charAt(i);

            if (caracterActual == caracter) {
                System.out.println("El caracter "+caracter+" está en la posición "+i);
            }

        }
    }
}
