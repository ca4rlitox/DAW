package ud3;

import java.util.Scanner;

public class H4Ej9 {
    public static void main(String[] args) {
        //Que lea 5 numeros por teclado, los copie a otro array multiplicados por 2 y muestre el segundo array

        // Definimos arrays y variables
        final int TAM = 2;
        int[] tabla1 = new int[5];
        int[] tabla2 = new int[5];
        int i=0;

        // Habilitamos escaner
        Scanner entrada = new Scanner(System.in);
        //Pedimos 5 numeros por teclado y hacemos bucle para hacer la multiplicacion x2 y que las guarde en el array tabla2
        System.out.println("Introduce 5 números para multiplicarlos x2");
        for (i = 0;i<5;i++) {
            tabla1[i] = entrada.nextInt();
            tabla2[i] = tabla1[i] * 2;
        }
        for (i=0;i<5;i++) {
            System.out.print(tabla2[i]+" ");
        }





    }
}
