package ud4;

import java.util.Scanner;

public class H5Ej21 {
    public static void main (String[] args) {
        Scanner entrada = new Scanner(System.in);
        //21. Que eleve un número cualquiera a una potencia cualquiera, mostrar en pantalla el resultado, se debe utilizar la recursividad.

        System.out.println("Escribe el numero");
        int numero = entrada.nextInt();
        System.out.println("Escribe potencia");
        int potencia = entrada.nextInt();

        potenciaRecursividad(numero,potencia);



    }

    public static void potenciaRecursividad (int a,int b) {
        int i=0;
        int resultado;

    }

}
