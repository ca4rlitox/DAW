package ud4;

import java.util.Scanner;

public class H5Ej14 {

    //Hacemos el escaner global
    static Scanner entrada = new Scanner(System.in);
    public static void main(String[] args) {

            /* 14. Que muestre una tabla de multiplicar de un número cualquiera por pantalla, el
    número se pedirá en el programa principal. */

        System.out.println("Escribe el número para saber su tabla de multiplicar");
        int valor1 = entrada.nextInt();
        multiplicar(valor1);

    }

    public static void multiplicar(int a) {

        for (int i=0;i<=10;i++) {
            System.out.println(a+" x "+i+" = "+(a * i));
        }

    }

    }
