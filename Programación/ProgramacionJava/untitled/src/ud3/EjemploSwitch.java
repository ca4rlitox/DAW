package ud3;

import java.util.Scanner;

public class EjemploSwitch {

    public static void main(String[] args) {

        //Habilitamos la lectura de datos por consola
        Scanner num=new Scanner(System.in);
        int opcion=0;
        do {
            System.out.println("Introduce una opcion");
            System.out.println("Para salir opcion 3");
            opcion = num.nextInt();
            //Alternativas múltiples

            switch (opcion) {
                case 1:
                    System.out.println("Opción 1");
                    break;
                case 2:
                    System.out.println("Opción 2");
                    break;
                case 3:
                    System.out.println("Opción 3. Has salido");
                    break;
                default:
                    System.out.println("Opción no válida");
            }
        } while (opcion != 3);




    }
}
