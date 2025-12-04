package ud5;

import java.util.Scanner;

public class H6B2Ej12 {
    public static void main (String[] args) {
        // 12. Contar el número de vocales de una frase.
        //Habilitamos escaner
        Scanner entrada = new Scanner(System.in);
        //Habilitamos variable de conteo
        int conteo=0;
        //Pedimos frase
        System.out.println("Introduce tu frase para saber cuantas vocales tiene");
        String cadena= entrada.nextLine();

        for (int i = 0;i<=cadena.length()-1;i++) {

            if (cadena.charAt(i) == 'a' || cadena.charAt(i) == 'e' ||cadena.charAt(i) == 'i' ||cadena.charAt(i) == 'o' ||cadena.charAt(i) == 'u'
                    ||cadena.charAt(i) == 'A'  ||cadena.charAt(i) == 'E' ||cadena.charAt(i) == 'I' ||cadena.charAt(i) == 'O' ||cadena.charAt(i) == 'U'){
                conteo++;
            }

        }

        System.out.println("Tu frase tiene "+conteo+" vocales.");


    }
}
