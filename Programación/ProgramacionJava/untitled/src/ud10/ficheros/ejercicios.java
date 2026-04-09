package ud10.ficheros;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;
import java.util.Scanner;

public class ejercicios {
    static Scanner entrada = new Scanner(System.in);
    static Random genAle = new Random();
    public static void main (String[] args) {
        EscribeFicheroNumRandom10();
    }

    public static void LeeFicheroInt100() {
        System.out.println("Ejercicio 2: ");
    }
    public static void EscribeFicheroNumRandom10() {
        FileWriter escritura;
        System.out.println("Ejercicio 1");
        try {
            System.out.println("Indica el nombre del fichero a escribir");
            escritura = new FileWriter(entrada.nextLine());
            for (int i = 0; i < 10; i++) {
                escritura.write(genAle.nextInt()+"\n");
            }
            escritura.close();
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
        System.out.println("Fin ejercicio 1\n");
    }
}
