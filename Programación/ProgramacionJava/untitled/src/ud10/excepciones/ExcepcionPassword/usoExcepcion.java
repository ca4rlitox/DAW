package ud10.excepciones.ExcepcionPassword;

public class usoExcepcion {

    public static void main (String[] args) throws excepcionLongitud, excepcionNumeros {


        try {
            verificarPasswd("uuu");
        } catch (excepcionNumeros e) {
            System.out.println(e.getMessage());
        }


    }

    public static void verificarPasswd(String pass) throws excepcionLongitud, excepcionNumeros {
        boolean longitud = false;
        boolean numeros = true;

        if (pass.length() == 8) { longitud = true; }

        for (int i = 0; i < pass.length(); i++) {
            char caracter = pass.charAt(i);
            if (caracter != '0' && caracter != '1' && caracter != '2' && caracter != '3' && caracter != '4'
                    && caracter != '5' && caracter != '6' && caracter != '7' && caracter != '8' && caracter != '9') {
                numeros = false;
                i=pass.length();
            }
        }
        if (!longitud && !numeros) {
            throw new excepcionLongitud("No tiene exactamente 8 caracteres y tiene caracteres que no son números.");
        }
        if (!longitud) {
            throw new excepcionLongitud("No tiene exactamente 8 caracteres.");
        }
        if (!numeros) {
            throw new excepcionNumeros("Contiene caracteres que no son números.");
        }

    }
}
