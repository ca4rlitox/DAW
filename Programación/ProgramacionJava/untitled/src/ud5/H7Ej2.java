package ud5;

import java.util.Random;

public class H7Ej2 {
    public static void main (String[] args) {
        // Escribe un programa que muestre la tirada de tres dados. Se debe mostrar también la suma total (los puntos que suman entre los tres dados).

        Random genAle = new Random();
        int suma=0;
        int numAle = genAle.nextInt(6)+1;
        int[] decimo = new int[5];

        for (int i = 0;i<3;i++) {
            int numAlea = genAle.nextInt(6)+1;
            System.out.println(numAlea);
            suma+= numAlea;
        }
        System.out.println("La suma de las tiradas es "+suma);

        for (int i = 0; i < 5; i++) {

            decimo[i] = genAle.nextInt(10);

        }
        for (int i = 0; i < 5; i++) {

            System.out.print("Tu decimo con suerte es el "+decimo[i]);
        }

    }
}
