package ud4;

import java.util.Scanner;

public class H4EjDeClase {
    public static void main(String[] args) {
        //Habilitamos lectura por teclado
        Scanner entrada = new Scanner(System.in);
        //Definimos variables y arrays
        final int TAM = 10;
        int [] nums = new int[11];
        int [] nums2 = new int [11];
        int [] res = new int [11];
        int i = 0;

        // Hacemos bucle para obtener valores para las dos tablas
        for (i=0;i<TAM;i++) {
            System.out.println("Introduce la primera tanda de números");
            nums[i] = entrada.nextInt();
        }
        for (i=0;i<TAM;i++) {
                System.out.println("Introduce la segunda tanda de números");
                nums2[i] = entrada.nextInt();
        }
        //Hacemos bucle para obtener los resultados multiplicando las tablas
        for (i=0;i<TAM;i++) {
            res[i] = nums[i] * nums2[i];
            // Mostramos el número multiplicado
            System.out.println(res[i]);
        }

    }
}
