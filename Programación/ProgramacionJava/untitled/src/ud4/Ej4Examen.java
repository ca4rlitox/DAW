package ud4;

import java.util.Scanner;

public class Ej4Examen {
    public static void main(String[] args) {

        //Habilitamos lectura por teclado
        Scanner entrada=new Scanner(System.in);
        //Definimos variable
        final int TAM = 500;
        char opcion;
        int par,impar;

        //Pedimos letra

            System.out.println("Introduzca p para saber los numeros pares e i para los impares.");
            opcion=entrada.nextLine().charAt(0);

        if ((opcion == 'p') || (opcion == 'P')) {
            for (par = 2; par < TAM + 1; par = par + 2) {
                System.out.println(par);
            }
        }

        else if ((opcion == 'i') || (opcion == 'I')) {
            for (impar = 1; impar < TAM; impar = impar + 2) {
                System.out.println(impar);
            }
        }

        else {
            System.out.println("Carácter introducido inválido. Intentalo otra vez.");
        }
    }
}
