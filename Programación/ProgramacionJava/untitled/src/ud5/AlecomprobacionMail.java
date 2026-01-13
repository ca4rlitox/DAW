package ud5;

public class AlecomprobacionMail {
    public static void main (String[] args) {
        String email="hola@pepe.com";

        if (comprobacionArroba(email) && comprobacionEspacio(email) && puntosSeguidos(email)) {
            System.out.println("Email correcto");
        }
        else {
            System.out.println("Email invalido");
        }

    }

    public static boolean comprobacionArroba (String email) {
        int arrobas=0;
        for (int i = 0; i < email.length(); i++) {
            if (email.charAt(i) == '@') {
                arrobas++;
            }
        }
        return arrobas == 1;
    }

    public static boolean comprobacionEspacio(String email) {
        char espacio=' ';
        for (int i = 0; i < email.length(); i++) {
            char letra = email.charAt(i);
            if (letra == espacio) {
                return false;
            }
        }
        return true;
    }

    public static boolean puntosSeguidos(String email) {
        String[] palabras = email.split("@");
        String despuesArroba = palabras[1];
        if (despuesArroba.indexOf('.') == despuesArroba.lastIndexOf('.')) {
            return true;
        }
        return false;
    }
}
