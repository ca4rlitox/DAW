package ud6;

import java.util.Random;

import static java.lang.Character.isLowerCase;
import static java.lang.Character.isUpperCase;

public class Password {
    int longitud;
    String contraseña;

    public Password() {
        contraseña=generaPasswd();
        longitud=contraseña.length();
    }

    public Password (String passwd) {
        longitud = passwd.length();
        this.contraseña = passwd;
    }

    public Password(int len) {
        contraseña="";
        Random genAle = new Random();
        String cadena = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890";
        for (int i = 0; i < len; i++) {
            char caracter = cadena.charAt(genAle.nextInt(cadena.length()));
            contraseña+=caracter;
        }
        longitud = contraseña.length();

    }

    //getters
    public String getContraseñayLength() {
        return contraseña+" "+longitud;
    }
    //setters
    public void  setLongitud(int len) {
        this.longitud = len;
    }
    public void setContraseña (String passwd) {
        this.contraseña = passwd;
        this.longitud = passwd.length();
    }

    public boolean esFuerte() {
        int mayus=0;
        int minus=0;
        int nums=0;
        for (int i = 0; i < longitud; i++) {
            char caracter=contraseña.charAt(i);
            if (isUpperCase(caracter)) {
                mayus++;
            }
            if (isLowerCase(caracter)) {
                minus++;
            }
            if (caracter == '1' || caracter == '2' || caracter == '3' || caracter == '4'  || caracter == '5'  || caracter == '6'
                    || caracter == '7'  || caracter == '8'  || caracter == '9'  || caracter == '0' ) {
                nums++;
            }
        }
        return mayus > 1 &&  minus > 0 && nums > 5;
    }

    public String generarPasswd (int len) {
        contraseña="";
        Random genAle = new Random();
        String cadena = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890";
        for (int i = 0; i < len; i++) {
            char caracter = cadena.charAt(genAle.nextInt(cadena.length()));
            contraseña+=caracter;
        }
        longitud = contraseña.length();
        return "OK";
    }

    public String generaPasswd () {
        String cad="";
        Random genAle = new Random();
        int longitud=genAle.nextInt(64);
        String cadena = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890";
        for (int i = 0; i < longitud; i++) {
            char caracter = cadena.charAt(genAle.nextInt(cadena.length()));
            cad+=caracter;
        }
        return cad;
    }

    public String toString() {
        return "Contraseña: "+contraseña+" longitud: "+longitud;
    }


}
