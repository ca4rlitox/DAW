package ud5;

import java.util.Random;

public class claseRandomEjemplo {
    public static void main (String[] args) {

        //Construimos objeto
        Random genAle = new Random();
        int [] frecuencia = new int[11];

        //generamos 100 numeros aleatorios
        for (int i = 0;i<1000000;i++) {
            int numAle = genAle.nextInt(11);
            frecuencia[numAle]++;
        }

        for (int i=0;i<11;i++) {
            System.out.println(i+" = "+frecuencia[i]+" veces (un "+(100*frecuencia[i]/1000000)+"%)");
        }
    }
}
