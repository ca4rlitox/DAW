package ud4;

import java.util.Scanner;

public class H4Ej16 {
    public static void main (String[] args) {
        //Definimos array bidimensional.
        int [][] matriz = new int [10] [10];
        int cien = 1;
        //Programa que muestre los primeros 100 números de izquierda a derecha usando un array de dos dimensiones.

        for (int i = 0;i<10;i++) {
            for (int j = 0;j<10;j++) {
                matriz[i][j] = cien;
                cien++;
            }
        }

        //Mostramos matriz
        for (int i = 0;i<10;i++) {
            for (int j = 0;j<10;i++) {
                System.out.print(matriz[j][i]+" ");
            }
        }








    }
}
