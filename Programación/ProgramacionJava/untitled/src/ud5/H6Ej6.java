package ud5;

import java.util.Scanner;

public class H6Ej6 {

    public static void main (String[] args) {
        // Realizar un programa que dada una cadena de caracteres por caracteres, genere otra cadena resultado de invertir la primera.

        //Habilitamos lectura por teclado
        Scanner entrada = new Scanner(System.in);
        String cadena;

        //Pedimos cadena
        System.out.println("Introduce la cadena");
        cadena = entrada.nextLine();
        System.out.println("El resultado de la cadena invertida es: "+aInvertido(cadena));
    }


    public static String aInvertido(String cadena) {

        String cadenaInvertida="";
        char caracter;

        for (int i = cadena.length()-1;i>=0;i--) {

            caracter=cadena.charAt(i);
            cadenaInvertida=cadenaInvertida+caracter;

        }
        return cadenaInvertida;
    }
}
