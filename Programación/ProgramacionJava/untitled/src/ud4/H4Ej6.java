package ud4;

import java.util.Scanner;

public class H4Ej6 {
    public static void main(String[] args) {

        //Habilitamos escaner
        Scanner entrada = new Scanner(System.in);
        //Definimos array y variables
        int[] num = new int[11];
        final int TAM = 10;
        int suma = 0;
        int resta = 0;
        int multiplicacion=1;
        double division=1;
        // Que lea 10 números por teclado, los almacene en un array y muestre la suma,
        //resta, multiplicación y división de todos.

        //Pedimos números hasta 10
        for (int i=0;i<TAM;i++) {
            System.out.println("Introduce un número hasta 10. Llevas " + i);
            num[i] = entrada.nextInt();
        }
        for (int i=1;i<TAM;i++) {
            num[i] = i;
            suma = num[i] + suma;
            resta = resta - num[i];
            multiplicacion = multiplicacion * num[i];
            division = division / num[i];

                System.out.println(num[i]);
            }
        System.out.println("Suma: "+suma);
        System.out.println("Resta: "+resta);
        System.out.println("Multiplicacion: "+multiplicacion);
        System.out.println("Division: "+division);
    }
}
