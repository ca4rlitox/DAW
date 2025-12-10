package ud5;

import java.util.Random;
import java.util.Scanner;

public class H7Ej13 {
    public static void main (String[] args) {
        // 13. El programa intentará adivinar el número que estás pensando – un número entre 0 y 100 –
        //teniendo para ello 5 oportunidades. En cada intento fallido, el programa debe preguntar si el
        //número que estás pensando es mayor o menor que el que te acaba de decir.
        Random genAle = new Random();
        Scanner entrada = new Scanner(System.in);
        char opcion;
        String menorOmayor="";
        int numAle;
        do{
            numAle=genAle.nextInt(100+1);
            System.out.println("El número que estás pensando es el "+numAle+"? (s/n)");
            opcion = entrada.nextLine().charAt(0);

            if (opcion == 'n') {
                System.out.println("El número es mayor o menor a ese número?");
                menorOmayor = entrada.nextLine();
                if (menorOmayor.equals("menor")) {
                int menol= genAle.nextInt(numAle);
                    System.out.println("tu numero es el "+menol+"? (s/n)");
                    opcion = entrada.nextLine().charAt(0);
                }
            }
        }while (opcion=='n');
        System.out.println("Sabía que tu número era el "+numAle);



    }
}
