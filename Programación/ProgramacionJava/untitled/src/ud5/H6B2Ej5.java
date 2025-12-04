package ud5;

import java.util.Scanner;

public class H6B2Ej5 {
    public static void main (String[] args) {
        // 5. Programa que pida un carácter c y un número n y que devuelva una cadena con c repetido n veces.
        //Habilitamos escaner
        Scanner entrada = new Scanner(System.in);

        //Pedimos caracter
        System.out.println("Introduce caracter que quieres repetir.");
        char caracter = entrada.nextLine().charAt(0);
        //Pedimos numero de repeticiones
        System.out.println("Introduce las veces que quieres que se repita.");
        int numVeces = entrada.nextInt();
        repeticiones(caracter,numVeces);

    }

    public static void repeticiones (int caracter, int numVeces) {
        String concatenacion="";
        for (int i = numVeces;i>0;i--) {
            concatenacion+=(char)caracter;
        }
        System.out.println(concatenacion);

    }
}
