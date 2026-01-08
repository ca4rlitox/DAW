package ud5;

import java.sql.SQLOutput;
import java.util.Random;
import java.util.Scanner;

public class H7Ej15 {
    public static void main (String[] args) {
        Scanner entrada = new Scanner(System.in);
        Random genAle = new Random();
        String[] posibilidades = {"corazón","diamante","herradura","campana","limon"};

        System.out.println("Escribe S para realizar la tirada, S para salir.");
        char opcion = entrada.nextLine().charAt(0);
        do{
            int numAle = genAle.nextInt(posibilidades.length);
            int numAle1 = genAle.nextInt(posibilidades.length);
            int numAle2 = genAle.nextInt(posibilidades.length);
            String tirada1 =  posibilidades[numAle];
            String tirada2 =  posibilidades[numAle1];
            String tirada3 =  posibilidades[numAle2];

            if (tirada1.equals(tirada2)|| tirada2.equals(tirada3)) {
                System.out.println("Enhorabuena, ha ganado 10 monedas");
            } else if (tirada1.equals(tirada2) || tirada2 != tirada3) {
                System.out.println("Bien, ha recuperado su moneda");
            }
            System.out.println(tirada1+tirada2+tirada3);
            System.out.println("¿Quiere tirar otra vez?");
            opcion=entrada.nextLine().charAt(0);
        }while(opcion!='S' || opcion!='s');




    }
}
