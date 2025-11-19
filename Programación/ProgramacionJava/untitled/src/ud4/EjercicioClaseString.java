package ud4;

import java.util.Scanner;

public class EjercicioClaseString {
    public static void main(String[] args) {

        Scanner entrada=new Scanner(System.in);

        System.out.println("Cuantas letras tiene tu palabra");
        int conteo = entrada.nextInt();
        entrada.nextLine();
        char array [] = new char [conteo];

        for (int i=0;i<conteo;i++) {

            System.out.println("Escribe tu palabra letra a letra:");
            array[i] = entrada.nextLine().charAt(0);

        }

        for (int i = 0;i<conteo;i++) {
            System.out.print(array[i]);
        }
        for (int i = conteo-1;i<conteo - 1;i--) {
            System.out.print(array[i]);
        }


    }
}
