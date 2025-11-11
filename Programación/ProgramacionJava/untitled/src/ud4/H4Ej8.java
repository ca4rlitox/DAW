package ud4;

import java.util.Scanner;

public class H4Ej8 {
    public static void main(String[] args) {
        // Definimos arrays
        int[] tabla1 = new int[5];
        int[] tabla2 = new int[5];
        int[] tablacompleta = new int[10];
        int cont = 0;

        // Enunciado: Que lea 10 números por teclado, 5 para un array y 5 para otro array distinto.
        // Mostrar los 10 números en otro array distinto.

        //Habilitamos escaner
        Scanner entrada = new Scanner(System.in);

        //Pdimos
        System.out.println("Introduce 5 numeros para la tabla 1");
        //Pedimos números
        for (int i = 0; i < 5; i++) {
            tabla1[i] = entrada.nextInt();
        }

        System.out.println("Introduce 5 numeros para la tabla 2");
        for (int i = 0; i < 5; i++) {
            tabla2[i] = entrada.nextInt();
        }

        for (int i=0;i<10;i++) {
            if (i<5) {
                tablacompleta[i] = tabla1[i];
            }else {
                tablacompleta[i] = tabla2[i-5];
            }
            System.out.println(tablacompleta[i]);
        }

    }
}