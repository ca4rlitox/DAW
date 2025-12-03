package ud5;

import java.util.Scanner;

import static java.lang.Character.*;

public class H6Ej8 {

    public static void main(String[] args) {

        //Habilitamos lectura por teclado
        Scanner entrada = new Scanner(System.in);
        //Habilitamos variables
        String cadena;

        //Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y viceversa

        //Pedimos cadena
        System.out.println("Escribe una cadena de texto");
        cadena = entrada.nextLine();

        System.out.println("Cadena convertida: " + comprobacionMayus(cadena));

    }

    public static String comprobacionMayus(String cad) {

        char caracter;
        String cadenaConvertida = "";

        for (int i = 0; i < cad.length(); i++) {
            caracter = cad.charAt(i);

            if (isUpperCase(caracter)) {
                caracter = toLowerCase(caracter);
                cadenaConvertida = cadenaConvertida + caracter;
            } else if (isLowerCase(caracter)) {
                caracter = toUpperCase(caracter);
                cadenaConvertida = cadenaConvertida + caracter;
            }
            else {
                cadenaConvertida = cadenaConvertida + caracter;
            }

        }

        return cadenaConvertida;

    }

}
