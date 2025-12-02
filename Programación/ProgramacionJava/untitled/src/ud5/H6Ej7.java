package ud5;

import java.util.Scanner;

public class H6Ej7 {
    public static void main (String[] args) {
        //Pide una cadena y dos caracteres por teclado (valida que sea un caracter), sustituye la aparicion del
        //primer caracter en la cadena por el segundo caracter.

        //Habilitamos variables
        char char1;
        char char2;
        String cad;
        String cadSustituida="";

        //Habilitamos escanner
        Scanner entrada = new Scanner(System.in);

        //Pedimos cadena por teclado
        System.out.println("Introduce cadena de texto: ");
        cad= entrada.nextLine();
        //Pedimos dos caracteres
        System.out.println("Introduce el caracter a ser sustituido");
        char1 = entrada.nextLine().charAt(0);
        if ((char1!='a') && (char1!='e') && (char1!='i') && (char1!='o') && (char1!='u')) {
            do{
                System.out.println("Caracter no valido. Prueba otra vez.");
                char1 = entrada.nextLine().charAt(0);
            }while ((char1!='a') && (char1!='e') && (char1!='i')&& (char1!='o')&& (char1!='u'));
        }
        System.out.println("Introduce el caracter que quieres poner");
        char2 = entrada.nextLine().charAt(0);
        if ((char2!='a') && (char2!='e') && (char2!='i') && (char2!='o') && (char2!='u')) {
            do{
                System.out.println("Caracter no valido. Prueba otra vez.");
                char2 = entrada.nextLine().charAt(0);
            }while ((char2!='a') && (char2!='e') && (char2!='i')&& (char2!='o')&& (char2!='u'));
        }

        for (int i = 0;i<cad.length();i++) {

            if (cad.charAt(i) == char1) {
                char2 = char2;
                cadSustituida = cadSustituida + char2;
            }
            else {
                cadSustituida= cadSustituida + cad.charAt(i);
            }


        }
        System.out.println(cadSustituida);

    }
}
