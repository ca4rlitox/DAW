package ud5;

import java.util.Arrays;
import java.util.Scanner;

public class EjercicioPreExamen2 {
    public static void main (String[] args) {
        /* Rellenar un array de 10 palabras leidas por teclado y mostrar:
        La palabra más larga y la más corta, OK
        La longitud media de las palabras, OK
        La palabra con mas vocales, OK
        Las palabras que terminan en consonante, OK
        Eliminar palabras duplicadas, independientemente si son mayusculas o minusculas.
        Ordenar el array alfabeticamente. OK
         */

        //Habilitamos lectura por teclado
        Scanner entrada = new Scanner(System.in);
        //Habilitamos array
        String[] palabras = new String[10];
        //Habilitamos las variables que vamos a usar de String
        String palabraMasLarga="";
        String palabraMasCorta="";
        String palabraConMasVocales="";
        String palabrasTerminadasEnConsonante="";
        //Habilitamos las variables que vamos a usar de int
        int palabraMesLarga=0;
        int palabraMesCorta=10;
        int media=0;
        int contadorVocales=0;
        int contadorVocalesAnterior=0;

        for (int i = 0; i < palabras.length; i++) {
            System.out.print("Introduce 10 palabras para rellenar el array, llevas "+i+":"+" ");
            palabras[i] = entrada.nextLine();

            char ultimaPosicion = palabras[i].charAt(palabras[i].length()-1);
            if (palabras[i].length() > palabraMesLarga) {
                palabraMesLarga = palabras[i].length();
                palabraMasLarga = palabras[i];
            }
            if (palabras[i].length() < palabraMesCorta) {
                palabraMesCorta = palabras[i].length();
                palabraMasCorta = palabras[i];
            }
            for (int j = 0; j < palabras[i].length(); j++) {
                if (palabras[i].charAt(j) == 'A' ||  palabras[i].charAt(j) == 'E' || palabras[i].charAt(j) == 'I' || palabras[i].charAt(j) == 'O' || palabras[i].charAt(j) == 'U' ||
                        palabras[i].charAt(j) == 'a' || palabras[i].charAt(j) == 'e' || palabras[i].charAt(j) == 'i' || palabras[i].charAt(j) == 'o' || palabras[i].charAt(j) == 'u') {
                    contadorVocales++;
                }
            }
            if (contadorVocales > contadorVocalesAnterior) {
                palabraConMasVocales=palabras[i];
                contadorVocalesAnterior=contadorVocales;
            }
            contadorVocales=0;

            if (ultimaPosicion != 'A' && ultimaPosicion != 'E' && ultimaPosicion != 'I' && ultimaPosicion != 'O' && ultimaPosicion != 'U' &&
                    ultimaPosicion != 'a' && ultimaPosicion != 'e' && ultimaPosicion != 'i' && ultimaPosicion != 'o' && ultimaPosicion != 'u'){
                palabrasTerminadasEnConsonante+=palabras[i]+" ";
            }
            media+=palabras[i].length();
        }
        //Aqui eliminamos las palabras repetidas
        int palabrasRepetidas=0;
        for (int i = 0; i < palabras.length; i++) {
            for (int j = 0; j < palabras.length; j++) {
                if (palabras[j].equals(palabras[i])) {
                    palabrasRepetidas++;
                }
                if (palabrasRepetidas>1) {
                    palabras[j] = "";
                }
                palabrasRepetidas=0;
            }

        }

        String []palabrasAcabadasConsonantes = new String [palabrasTerminadasEnConsonante.split(" ").length];
        palabrasAcabadasConsonantes = palabrasTerminadasEnConsonante.split(" ");

        for (int i = 0; i < palabrasAcabadasConsonantes.length; i++) {
            System.out.println("Palabras acabada en consonante: "+palabrasAcabadasConsonantes[i]);
        }

        media = media/palabras.length;
        Arrays.sort(palabras);
        System.out.println("La palabra mas larga es: "+palabraMasLarga+" y la mas corta es: "+palabraMasCorta+" y la media es de: "+media+", la palabra con mas vocales es: "+palabraConMasVocales);












    }
}
