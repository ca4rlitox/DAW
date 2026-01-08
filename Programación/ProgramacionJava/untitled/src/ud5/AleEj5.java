package ud5;

import java.util.Random;

public class AleEj5 {
    public static void main (String[] args) {
        Random genAle = new Random();
        int suma=0;
        int max=0;
        int min=200;

        for (int i = 0; i < 50; i++) {
            int numAle = genAle.nextInt(101)+100;
            System.out.print(numAle+" ");
            suma+=numAle;

            if (numAle > max) {
                max = numAle;
            }
            if (numAle < min) {
                min=numAle;
            }

        }
        System.out.println();
        System.out.println("La suma es: "+suma);
        System.out.println("La media es: "+suma/50);
        System.out.println("El número mas pequeño es el: "+min);
        System.out.println("El número mas grande es el: "+max);



    }
}
