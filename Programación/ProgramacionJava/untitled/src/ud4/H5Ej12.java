package ud4;

import java.util.Scanner;

public class H5Ej12 {
    //Constante globale
    static final int TAM=5;
    //Global el escaner
    static Scanner entrada = new Scanner(System.in);

    public static void main(String[] args) {

        // 12. Que rellene un array de 20 enteros, utilizar una función.
        int[] numeros = rellenaArray();

        //Mostramos el array
        for (int i=0;i<TAM;i++) {
            System.out.print(numeros[i]+", ");
        }

    }

    public static int[] rellenaArray () {

        int[] nums = new int[TAM];
        for (int i = 0;i<TAM;i++) {
            System.out.println("Introduce los numeros para el array");
            nums[i] = entrada.nextInt();
        }
        return nums;

    }

}
