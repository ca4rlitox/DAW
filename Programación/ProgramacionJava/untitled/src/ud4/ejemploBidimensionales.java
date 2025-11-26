package ud4;

import java.util.Scanner;

public class ejemploBidimensionales {
    static Scanner entrada=new Scanner(System.in);

    public static void main (String[] args) {

        int[][] matriz = new int [2][3];

        for (int i = 0;i<2;i++) {
            for (int j = 0;i<3;i++) {
                System.out.println("Introduce un número: ");
                matriz[i][j] = entrada.nextInt();
            }
        }
        for (int i = 0;i<2;i++) {
            for (int j = 0;i<3;i++) {
                System.out.println(matriz[i][j]+" ");
            }
            System.out.println();
        }

    }
}
