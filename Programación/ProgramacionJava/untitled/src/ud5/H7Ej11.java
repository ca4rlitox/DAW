package ud5;

import java.util.Random;

public class H7Ej11 {
    public static void main (String[] args) {
        // 11. Escribe un programa que muestre 20 notas generadas al azar. Las notas deben aparecer de la
        //forma: suspenso, suficiente, bien, notable o sobresaliente. Al final aparecerá el número de
        //suspensos, el número de suficientes, el número de bienes, etc.

        //Habilitamos random
        Random genAle = new Random();

        //Habilitamos array con notas posibles
        String [] calificacionesPosibles = {"Suspenso","Suficiente","Bien","Notable","Sobresaliente"};
        int numAle;
        int insuficiente=0;
        int suficiente=0;
        int bien=0;
        int notable=0;
        int sobresaliente=0;

        for (int i = 0;i<20;i++) {
            numAle = genAle.nextInt(5);
            System.out.println(calificacionesPosibles[numAle]);
            if (numAle == 0) {
                insuficiente++;
            }
            else if (numAle == 1) {
                suficiente++;
            }
            else if (numAle == 2) {
                bien++;
            }
            else if (numAle == 3) {
                notable++;
            }
            else if (numAle == 4) {
                sobresaliente++;
            }
        }
        System.out.println("\nNumero de suspensos: "+insuficiente+" "+(100*insuficiente/20)+"%"+
                "\nNumero de suficientes: "+ suficiente +" "+(100*suficiente/20)+"%"+
                "\nNumero de bienes: "+ bien +" "+(100*bien/20)+"%"+
                "\nNumero de notables: "+ notable +" "+(100*notable/20)+"%"+
                "\nNumero de sobresalientes: "+sobresaliente+" "+(100*sobresaliente/20)+"%");


    }
}
