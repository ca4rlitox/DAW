package ud5;

import java.util.Scanner;

public class H6Ej11 {
    public static void main(String[] args) {

        // Realizar una función a la que se le pasa por parámetro una cadena con un email, y dicha función devuelve si el mail está bien formado.
        // Un email está bien formado cuando:
        // Contiene una y solo una arroba.
        // No puede contener dos puntos seguidos '.' después de la arroba.
        // No puede contener ''

        //Habilitamos escaner
        Scanner entrada = new Scanner(System.in);
        //Habilitamos variable
        String email;

        System.out.println("Introduce un mail para validarlo.");
        email = entrada.nextLine();

        if ((unArroba(email)) && (dosPuntosSeguidos(email) && contieneEspacio(email))) {
            System.out.println("Mail validado correctamente.");
        } else {
            System.out.println("Mail incorrecto.");
        }

    }

    public static boolean unArroba(String arroba) {
        if (arroba.indexOf('@') == arroba.lastIndexOf('@') && (arroba.indexOf('@') != -1) && (arroba.lastIndexOf('@') != -1)) {
            return true;
        }
        return false;
    }

    public static boolean dosPuntosSeguidos(String puntosSeguidos) {

        String[] separador = puntosSeguidos.split("@");
        String palabra = separador[1];

        for (int i = separador.length - 1; i != 0; i--) {
            if ((palabra.charAt(0) & palabra.charAt(1)) == '.') {
                return false;
            }
        }
        return true;
    }

    public static boolean contieneEspacio (String contieneEspacio) {
        if (contieneEspacio.indexOf(" ") == -1) {
            return true;
        }
        return false;
    }
}