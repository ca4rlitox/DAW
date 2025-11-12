package ud4;

import java.util.Scanner;

public class H5Ej12 {
    //Constante globale
    static final int TAM=20;
    //Global el escaner
    static Scanner entrada = new Scanner(System.in);

    public static void main(String[] args) {

        int[] numeros = new int[TAM];
        // 12. Que rellene un array de 20 enteros, utilizar una función.

        for (int i=0;i<TAM;i++) {
            rellenaArray();
        }
        System.out.print(numeros);

    }

    public static int[] rellenaArray () {

        int[] vente = new int[TAM];
        for (int i = 0;i<TAM;i++) {
            System.out.println("Introduce los numeros para el array");
            vente[i] = entrada.nextInt();
        }

        return vente;

    }

}
