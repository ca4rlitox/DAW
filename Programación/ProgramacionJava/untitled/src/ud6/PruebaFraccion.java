package ud6;

import java.util.Scanner;

public class PruebaFraccion {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.println("Introduce numerador y denominador de f1:");
        Fraccion f1 = new Fraccion(entrada.nextInt(),entrada.nextInt());

        System.out.println("Introduce numerador y denominador de f2:");
        Fraccion f2 = new Fraccion(entrada.nextInt(),entrada.nextInt());

        System.out.println(f1+"+"+f2+"="+f2.sumaFraccion(f1));





    }
}
