package ud4;

import java.util.Scanner;

public class H5Ej11 {
    public static void main(String[] args) {
        // 11. Que muestre por pantalla si un número es par o impar, utilizar una función.
        Scanner entrada = new Scanner(System.in);

        System.out.println("Indica el número para saber si es par o impar");
        int x = entrada.nextInt();
        System.out.println(parOimpar(x));

    }

    public static int parOimpar(int a) {

        int rsdo = a % 2;
        if (rsdo == 0) {
            System.out.println("Es par");
        }

        else{
            System.out.println("Es impar");
        }
        return rsdo;
    }

}
