package ud5;

import java.util.Scanner;

public class H6B2Ej14 {
    public static void main (String[] args) {
        /*14. Sustituir todos los espacios de una frase por * (sin usar replace). Pedir una frase y un carácter,
        escribir en pantalla la frase inicial pero sólo hasta la primera aparición del carácter dado (sin
        incluirlo). No se puede utilizar indexOf.*/

        //Habilitamos escaner
        Scanner entrada = new Scanner(System.in);
        //Habilitamos variables
        char asterisco='*';
        char caracter;
        String cadenaSustituida="";
        //Pedimos frase
        System.out.println("Introduce frase: ");
        String cadena = entrada.nextLine();
        System.out.println("Introduce el caracter final para que pare la frase.");
        char fin = entrada.nextLine().charAt(0);

        for (int i = 0;i<=cadena.length()-1;i++) {
            caracter=cadena.charAt(i);
            if (caracter==fin){
                break;
            }
            if (caracter == ' '){
               cadenaSustituida+=asterisco;
            }
            else {
                cadenaSustituida+=caracter;
            }
        }
        System.out.println(cadenaSustituida);

    }
}
