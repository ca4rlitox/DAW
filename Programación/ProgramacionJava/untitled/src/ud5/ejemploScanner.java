package ud5;

import java.util.Scanner;

public class ejemploScanner {

    public static void main(String[] args) {

        //Construyo un objeto
        Scanner scanner;


        scanner=new Scanner(System.in);

        System.out.println("Introduce un numero");
        boolean esEntero=scanner.hasNextInt();

        if (esEntero) {
            System.out.println("Es entero");
        }

        else {
            do {
                System.out.println("No es entero.");
                scanner.nextLine();
                System.out.println("Introduce un numero");
                esEntero=scanner.hasNextInt();


            } while (!esEntero);
            System.out.println("Es entero");


        }
    }

}
