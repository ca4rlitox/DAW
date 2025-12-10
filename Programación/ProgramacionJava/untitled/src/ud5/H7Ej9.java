package ud5;

import java.util.Random;

public class H7Ej9 {
    public static void main (String[] args) {
        //9. Realiza un programa que vaya generando números aleatorios pares entre 0 y 100 y que no
        //termine de generar números hasta que no saque el 24. El programa deberá decir al final cuántos
        //números se han generado.

        //Habilitamos random
        Random genAle = new Random();
        //Habilitamos variable
        int num = 0;
        int nummAle;
        int i=0;

        //Hacemos bucle para generar numeros hasta que salga el 24
        int numAle;
        do {
            numAle = genAle.nextInt(100)+1;
            if (numAle % 2 == 0) {
                num++;
                i++;
                System.out.println(i + ". " + numAle);
            }
        } while (numAle != 24);
        System.out.println("Ha salido el 24 tras " + i + " tiradas!");
    }
}
