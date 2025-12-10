package ud5;

import java.util.Random;

public class H7Ej8 {
    public static void main (String[] args) {
        // 8. Modifica el programa anterior para que la probabilidad de que salga un 1 sea de 1/2, la
        //probabilidad de que salga x sea de 1/3 y la probabilidad de que salga 2 sea de 1/6. Pista: 1/2 = 3/6 y 1/3 = 2/6.

        //Habilitamos random
        Random getAle = new Random();
        //Habilitamos variable random para que coja un numero del 0 al 10 para que coja el resultado del array.
        int plenoalquinceAle = getAle.nextInt(10);

        //Habilitamos el array de partidos
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
        //Habilitamos el array de resultados del pleno al 15
        String [] plenoal15 = {
                "0-0", "1-0", "0-1", "1-1","2-1", "1-2", "2-2","3-2", "2-3", "3-3"};

        //Habilitamos el array de resultados de las 14 primeros.
        String[] resultadosal14 = {
                "1",
                "1",
                "1",
                "X",
                "X",
                "2"
        };

        // Hacemos bucle para que salga con aleatoriedad el resultado de los 14 primeros.
        for (int i = 0; i < partidos.length; i++) {
            int tresAle = getAle.nextInt(6);
            System.out.println(partidos[i] + " - " + resultadosal14[tresAle]);
        }

        //Fuera del bucle ponemos la tirada al 15, ya que queremos que solo salga una vez
        System.out.println("\nPleno al 15: " + partidos[plenoalquinceAle] + " = " + plenoal15[plenoalquinceAle]);
    }
}
