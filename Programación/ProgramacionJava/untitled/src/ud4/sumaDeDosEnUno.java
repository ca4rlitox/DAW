package ud4;

import java.util.Scanner;

public class sumaDeDosEnUno {

    public static void main(String[] args) {

        int[] cajon1 = new int [5];
        int[] cajon2 = new int [5];
        Scanner in = new Scanner(System.in);

        for (int i = 0;i<cajon1.length;i++) {
            cajon1[i]= in.nextInt();
        }

        for (int i = 0;i<cajon2.length;i++) {
            cajon2[i]= in.nextInt();
        }

        suma(cajon1,cajon2);

    }

    public static void suma(int[]a,int[]b) {

        for (int i = 0;i<5;i++) {
            a[i] = a[i] + b[i];
        }

        for (int i = 0;i<5;i++) {
            System.out.println(a[i]);
        }


    }

    }
