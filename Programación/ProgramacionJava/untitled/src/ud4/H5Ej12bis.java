package ud4;

import java.util.Scanner;

public class H5Ej12bis {
    //Constante globales
    static final int TAM=5;
    //Global el escaner
    static Scanner entrada = new Scanner(System.in);

    public static void main(String[] args) {
        // Cualquier valor se pasa por referencia

        int[] numeros=new int[TAM];

        rellena(numeros);
        for (int i=0;i<TAM;i++) {
            System.out.println(numeros[i]);
        }

    }

    public static void rellena(int[] nums) {

        for (int i=0;i<TAM;i++) {
            System.out.println("Introduce número: ");
            nums[i]= entrada.nextInt();
        }
    }
}
