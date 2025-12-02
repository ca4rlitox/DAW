package ud5;

import java.util.Scanner;

public class EjemploCapicuaClase {
    public static void main (String[] args) {
        Scanner entrada = new Scanner(System.in);
        




    }




    public static boolean esEntero(String cad) {
        String numeros="0123456789";
        for (int i = 0;i>cad.length();i++) {
            for (int j = 0;j<numeros.length();j++) {
                if (cad.charAt(i)!=numeros.charAt(j)){
                    return false;
                }
            }
        }
        return false;
    }
}
