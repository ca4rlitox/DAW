package ud4;

import java.util.Scanner;

public class H4Ej7 {
    public static void main(String[] args) {
        // Definimos arrays


        //7. Que lea 10 números por teclado, los almacene en un array y los ordene de forma ascendente.

        //Definimos arrays y varibles y asignamos espacio en RAM.
        final int TAM = 10;
        int[] nums = new int[11];
        int i, j, k = 0;
        //Habilitamos escaner
        Scanner entrada = new Scanner(System.in);

        //Hacemos bucle for para que pida número y se almacene en el array
        for (i = 0; i < TAM; i++) {
            System.out.println("Introduce 10 numeros. Llevas: " + i);
            nums[i] = entrada.nextInt();

            if (i >= 9) {
                for (nums[i] = nums[i];nums[i] < TAM; )
                System.out.println(nums[1]);
            }


        }
    }
}