package ud4;

import java.util.Scanner;

public class H5Ej7 {

    static Scanner in = new Scanner(System.in);

    public static void main(String[] args) {

        mostarMenu();
        System.out.println("Elige una opción");
        int opcion = in.nextInt();

        System.out.println("Introduce el primer número");
        int num1 = in.nextInt();

        System.out.println("Introduce el segundo número");
        int num2 = in.nextInt();

        if (opcion == 1) {
            sumar(num1, num2);
        }

        if (opcion == 2) {
            restar(num1, num2);
        }

        if (opcion == 3) {
            multiplicar(num1, num2);
        }

        if (opcion == 4) {
            dividir(num1, num2);
        }
    }


    public static void mostarMenu() {
        System.out.println("1. Sumar, 2. Restar, 3. Multiplicar, 4. Dividir");
    }

    public static void sumar(int a, int b) {
        int resultado;
        resultado = a + b;
        System.out.println("La suma es " + resultado);
    }

    public static void restar(int a, int b) {
        int resultado;
        resultado = a - b;
        System.out.println("La resta es " + resultado);
    }

    public static void multiplicar(int a, int b) {
        int resultado;
        resultado = a * b;
        System.out.println("La multiplicación es " + resultado);
    }

    public static void dividir(int a, int b) {
        double resultado;
        resultado = (double) a / b;
        System.out.println("La división es " + resultado);
    }

}