package ud6;

import java.util.Scanner;

public class PruebaFraccion2 {
    public static void main(String[] args) {
        Fraccion[] f1 = new Fraccion[10];
        Scanner entrada = new Scanner(System.in);


        for (int i = 0; i < 10; i++) {
            System.out.println("Introduce numerador y denominador de la fraccion f" + i);
            f1[i] = new Fraccion(entrada.nextInt(), entrada.nextInt());
        }

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 10; j++) {
            System.out.println(i+"."+j+" Suma de " + f1[i] + "+" + f1[j] + "=" + f1[i].sumaFraccion(f1[j]));
            System.out.println(i+"."+j+" Resta de " + f1[i] + "-" + f1[j] + "=" + f1[i].restaFraccion(f1[j]));
            System.out.println(i+"."+j+" Multiplicacion de " + f1[i] + "*" + f1[j] + "=" + f1[i].multiplicaFraccion(f1[j]));
            System.out.println(i+"."+j+" Division de " + f1[i] + "/" + f1[j] + "=" + f1[i].divideFraccion(f1[j]));
        }
    }

    }
}
