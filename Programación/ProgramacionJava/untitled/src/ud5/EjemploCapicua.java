package ud5;

import java.util.Scanner;

public class EjemploCapicua {
    public static void main (String[] args) {

        //Determinar si un numero es capicua con metodos
        //Habilitamos lectura por teclado.
        Scanner entrada = new Scanner(System.in);

        int j=0;
        boolean capicua=false;

                //Pedimos cadena de numeros para ver si es capicua
        System.out.println("Introduce un número para determinar si es capicua");
        String capicuaOno= entrada.nextLine();

        //Hacer un bucle for comparando del ultimo a la mitad
        for (int i = capicuaOno.length()-1;i>0;i--, j++) {
            char a = capicuaOno.charAt(j);
            char b = capicuaOno.charAt(i);
            if (a == b) {
                capicua = true;
            }
            else {
                capicua = false;
            }
        }
        if (capicua) {
            System.out.println("Es capicua");
        }
        else {
            System.out.println("No es capicua");
        }

    }
}
