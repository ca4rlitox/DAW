package ud5;

import java.util.Scanner;

public class EjemploLeerCadena {
    public static void main (String[] args) {
        //Habilitamos lectura por teclado
        Scanner entrada = new Scanner(System.in);
       // Leer una cadena por teclado, almacenarla y mostrarla al reves.
        String cadena=new String();
        String cadenainvertida="";

        System.out.println("Introduce la cadena de texto: ");
        cadena = entrada.nextLine();

        if (cadena.isEmpty()) {
            System.out.println("La cadena está vacia. Introduce otra vez el texto");
            cadena = entrada.nextLine();
        }
        else {
            for (int i = cadena.length()-1;i>=0;i--) {

                cadenainvertida=cadenainvertida+cadena.charAt(i);

            }
            System.out.println(cadenainvertida);
        }


    }
}
