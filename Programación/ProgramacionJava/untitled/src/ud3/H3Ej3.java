package ud3;

import java.util.Scanner;

public class H3Ej3 {
    public static void main(String[] args) {
        // Números Primos Gemelos. Desarrolla un programa que encuentre y muestre todos los
        // pares de "números primos gemelos" en un rango dado. Los números primos gemelos son dos
        // números primos que difieren en 2 unidades. Por ejemplo, 41 y 43 son un par de números
        // primos gemelos

        // Habilitamos escaner
        Scanner sc = new Scanner(System.in);

        // Definimos variables

        int a=1;
        int b=0;

        //Pedimos numeros

        int num= sc.nextInt();

        for (int i=2;i < num - 1;i++) {

            a = num % i;

            if (a == 0) {
            b = b + a;
            }

        }
        if (b == 0) {
            System.out.println("El número es primo");
        }
    }
}
