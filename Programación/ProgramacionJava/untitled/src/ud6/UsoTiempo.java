package ud6;

import java.util.Scanner;

public class UsoTiempo {

    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Introduce hora: ");
        int h = sc.nextInt();
        System.out.print("Introduce minuto: ");
        int m = sc.nextInt();
        Tiempo t = new Tiempo(h,m,0);
        System.out.println(t);
        }
    }
