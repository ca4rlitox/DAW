package ud5;

import java.util.Random;

public class H7Ej4 {
    public static void main (String[] args) {
        //Escribe un programa que muestre al azar el nombre de una carta de la baraja española.
        // Esta baraja esta dividida en tres palos: sota, caballo y rey.
        //Cada palo está formado por 13 cartas, de las cuales 9 cartas son numerales y 4 literales.
        //2,3,4,5,6,7,8,9,10,J,Q,K,A (que sería el 1). Para convertir un número en una cadena de caracteres
        //podemos usar CONVERTIRATEXTO (String.valueOf(n) en JAVA).

        String[] palo= {"oros","copas","bastos","espadas"};
        String[] numero={"2","3","4","5","6","7","sota","caballo","rey","as"};
        Random genAle = new Random();
        int paloAle = genAle.nextInt(palo.length);
        int numAle = genAle.nextInt(numero.length);

        System.out.println("Numero: "+numero[numAle]+" palo: "+palo[paloAle]);
    }
}
