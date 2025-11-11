package ud3;

import java.util.Scanner;

public class H3Ej1 {
    public static void main(String[] args) {

        // Realiza un método que, dado un número de tres cifras, averigüe si es un número Armstrong
        //o Narcisista. Un número es Armstrong cuando la suma de cada uno de los números que lo
        //componen elevado al número de dígitos de dicho número de dicho número da como resultado
        //el propio número. Ejemplo de un número de 3 dígitos: 153=1elevado(3)+5elevado(3)+3elevado(3)

        // Habilitamos escaner

        Scanner sc = new Scanner(System.in);

        // Inicializamos la variable
        int entero = 0;
        // Pedimos un número

        System.out.println("Introduce el número dígito a dígito para saber si es narcicista");
        int num = sc.nextInt();
        int num2 = sc.nextInt();
        int num3 = sc.nextInt();

        entero = (num * 100) + (num2 * 10) + (num3);

        if ((num * num * num) + (num2 * num2 * num2) + (num3 * num3 * num3) == entero) {

            System.out.println("Es un número narcicista");

        }

        else {
            System.out.println("No es un número narcicista");
        }

    }
}
