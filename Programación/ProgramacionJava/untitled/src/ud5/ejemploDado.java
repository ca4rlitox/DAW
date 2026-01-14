package ud5;

import java.util.Random;

public class ejemploDado {
    public static void main (String[] args) {
        int[] frecuencia = new int [6];
        Random genAle = new Random();


        //generamos 100 numeros aleatorios
        for (int i = 0;i<10000;i++) {
            int tirada = genAle.nextInt(6) + 1;
            frecuencia[tirada - 1]++;
        }
        for (int i = 0;i<100;i++) {
            System.out.println((i+1)+":"+frecuencia[i]+":"+(100.0*frecuencia[i]/10000)+"%");
        }
    }
}
