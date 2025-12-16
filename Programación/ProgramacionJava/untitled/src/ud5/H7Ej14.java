package ud5;

import java.util.Random;
import java.util.Scanner;

public class H7Ej14 {
    public static void main (String[] args) {

        Scanner entrada = new Scanner(System.in);
        Random genAle = new Random();
        String[] notas = {"do","re","mi","fa","sol","la","si"};
        String primeraNota="";
        int cuatro=4;

        System.out.println("Escribe cuantos compases quieres generar:");
        int compases = entrada.nextInt();

        for (int k = 0; k < compases; k++) {
            for (int i = 0; i < cuatro; i++) {
                int numAle = genAle.nextInt(notas.length);
                if (i==0 & k==0){
                    primeraNota=notas[numAle];
                    System.out.print(notas[numAle]+" ");
                }
                else if (k == compases -1 && i == cuatro-1) {
                    System.out.print(primeraNota+" ");
                }
                else {
                    System.out.print(notas[numAle]+" ");
                }
                }
            System.out.print("| ");
        }
            System.out.print("|");
        }
    }
