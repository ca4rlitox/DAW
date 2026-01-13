package ud5;

import java.util.Random;
import java.util.Scanner;

public class AleEj9 {
    public static void main (String[] args) {
        Random genAle = new Random();
        Scanner entrada = new Scanner(System.in);
        int numAle = genAle.nextInt(100);
        System.out.println(numAle);
    }
}
