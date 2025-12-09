package ud5;

import java.util.Random;

public class H7Ej7 {
    public static void main (String[] args) {
        //7. Escribe un programa que muestre tres apuestas de la quiniela en tres columnas para los 14
        //partidos y el pleno al quince (15 filas).

        Random getAle = new Random();

        int plenoalquinceAle = getAle.nextInt(10);


        String[] partidos = {
                "Real Madrid vs Barcelona",
                "Atletico Madrid vs Valencia",
                "Sevilla vs Villarreal",
                "Betis vs Real Sociedad",
                "Athletic Club vs Osasuna",
                "Getafe vs Rayo Vallecano",
                "Celta de Vigo vs Girona",
                "Mallorca vs Alavés",
                "Las Palmas vs Cádiz",
                "Espanyol vs Tenerife",
                "Zaragoza vs Sporting de Gijón",
                "Granada vs Levante",
                "Elche vs Valladolid",
                "Huesca vs Leganés",
                "Valencia vs Getafe"
        };

        String [] plenoal15 = {
                "0-0", "1-0", "0-1", "1-1","2-1", "1-2", "2-2","3-2", "2-3", "3-3"};

        String[] resultadosal14 = {
                "1",
                "X",
                "2",
        };

        for (int i = 0; i < partidos.length; i++) {
            int tresAle = getAle.nextInt(3);
            System.out.println(partidos[i] + " - " + resultadosal14[tresAle]);
        }
        System.out.println("\nTirada al 15: " + partidos[plenoalquinceAle] + " - " + plenoal15[plenoalquinceAle]);
    }
}
