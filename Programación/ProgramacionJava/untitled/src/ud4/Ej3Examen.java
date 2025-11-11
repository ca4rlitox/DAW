package ud4;

import java.util.Scanner;

public class Ej3Examen {
    public static void main(String[] args) {

        //Habilitamos lectura por teclado
        Scanner entrada=new Scanner(System.in);
        //Definimos variables
        int num1=-1,num2=-1,escalones;

        // Pedimos números
        do {
            System.out.println("Introduce el primer número. Debe estar entre el 0 y el 100");
            num1 = entrada.nextInt();
            System.out.println("Introduce el segundo número. Debe estar entre el 0 y el 100");
            num2 = entrada.nextInt();
        } while ((num1 < 0) || (num1 >100) || (num2 <0) || (num2 >100));

        //En caso de que el primer número sea mayor que el segundo
        if (num1 > num2) {
            // Hacemos con un bucle for que vaya del num1 (el mayor) hasta el num2 incluido (menor) DESC
            for (escalones = num1; escalones > num2 - 1; escalones--) {
                System.out.print(escalones + " ");
            }
        }
        //En caso de que el segundo número sea mayor que el primero
        else if (num1 < num2) {
            // Hacemos con un bucle for que vaya del num1 (el menor) hasta el num2 incluido (mayor) ASC
            for (escalones=num1;escalones<num2 + 1;escalones++){
                System.out.print(escalones+" ");
            }
        }


    }
}
