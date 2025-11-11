package ud3;

import java.util.Scanner;

public class H2Ej1 {
    public static void main(String[] args) {

    // Habilitamos lectura por teclado
        Scanner entrada=new Scanner(System.in);
    //ZDV
        int c = 2;
        int primoono=0;
        int siprimo=0;

        // Pedimos numero
        System.out.println("Introduce un número para saber si es primo");
        int num = entrada.nextInt();

    for (num=num;c<num-1;c++) {

        primoono = num % c;
        if (primoono == 0) {
            siprimo++;
        }

        }
        if (siprimo != 0) {
            System.out.println("El número no es primo");
        }
        if (siprimo == 0) {
            System.out.println("El numero es primo");
        }

        }

    }


