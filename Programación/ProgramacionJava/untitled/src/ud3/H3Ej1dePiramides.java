package ud3;

import java.util.Scanner;

public class H3Ej1dePiramides {
    public static void main(String[] args) {

        //Habilitamos escaner
        Scanner sc = new Scanner(System.in);

        // Definimos variables
        int ast = 0;

        System.out.println("Introduce el número de filas que quieres para la piramide");
        int filas = sc.nextInt();
        int cont = 0;
        int fila = filas;


        for (fila = 1; fila <= filas; fila++) {
            for (int c = 1; c <= fila; c++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }

}

