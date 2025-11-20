package ud4;

import java.util.Scanner;

public class vocalOno {
    public static void main(String[] args) {

        //Habilitamos escaner
        Scanner in = new Scanner(System.in);

        //Definimos variable
        char opcion;

        System.out.println("Pon letra para ver si es vocal");
        opcion = in.nextLine().charAt(0);


        if (!esVocal2(opcion)) {
            System.out.println("No es vocal");
        }
        else{
            System.out.println("Es vocal");
        }

    }



    public static boolean esVocal(char letra) {

        if ((letra=='A') || (letra=='E') || (letra=='I') || (letra=='O') || (letra=='U') || (letra=='a') || (letra=='e') || (letra=='i') || (letra=='o') || (letra=='u')) {
            return true;
        }
        else return false;
    }

    public static boolean esVocal2(char letra) {
        char[] vocales ={'a','e','i','o','u','A','E','I','O','U'};

        for (int i=0;i<vocales.length;i++) {
            if (vocales[i] == letra) {
                return true;
            }
        }
        return false;
    }
}
