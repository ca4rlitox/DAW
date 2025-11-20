package ud4;

import java.util.Scanner;

public class sumaDeDos {
    public static void main(String[] args) {

        int[]cajon1={1,2,3,4,5};
        int[]cajon2={1,2,3,4,5};
        int[] resultado=suma(cajon1,cajon2);

        for (int i = 0;i<5;i++) {
            System.out.println(resultado[i]);
        }

    }

    public static int[] suma (int[]a,int[]b) {
        int[] rsdo = new int[5];

        for (int i = 0;i<5;i++) {
            rsdo[i] = a[i] + b[i];
        }

return rsdo;
    }
}
