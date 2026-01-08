package ud5;

import java.util.Random;
import java.util.Scanner;

public class AleEj6 {
    public static void main (String[] args) {
        Random genAle = new Random();
        Scanner entrada = new Scanner(System.in);
        int numAle = genAle.nextInt(101);
        int oportunidades=0;
        int numIntroducido;

        System.out.println("Voy a pensar un número entre el 0 y el 100. Intenta adivinarlo: ");
        numIntroducido = entrada.nextInt();
        if (numIntroducido != numAle) {
            do {
                System.out.println("El número no es "+numIntroducido+".");
                if (oportunidades > 4) {
                    System.out.println("Has perdido al consumir todas las oportunidades. El número era el "+numAle);
                    break;
                }
                else if (numIntroducido > numAle) {
                    System.out.println("El número que estoy pensando es menor que el introducido.");
                    numIntroducido = entrada.nextInt();
                    oportunidades++;
                }
                else if (numIntroducido < numAle) {
                    System.out.println("El número que estoy pensando es mayor que el introducido.");
                    numIntroducido = entrada.nextInt();
                    oportunidades++;
                }
                else {
                    System.out.println("Has adivinado el número!");
                    System.out.println("Has introducido el "+numIntroducido+" y era el "+numAle);
                    break;
                }
            }while (numIntroducido != numAle);
            if (numIntroducido==numAle) {
                System.out.println("Has adivinado el número!");
                System.out.println("Has introducido el "+numIntroducido+" y era el "+numAle);
            }
        }
        else {
            System.out.println("Has adivinado el número! Era: "+numAle);
        }

    }
}
