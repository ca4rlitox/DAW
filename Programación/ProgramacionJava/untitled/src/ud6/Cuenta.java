package ud6;

import java.util.Random;

public class Cuenta {
    private String DNI, nCuenta;
    private double saldo;
    private Cuenta[] cuentas = new Cuenta[3];


    public Cuenta() {


    }

    //setters
    public void setDNI(String documento) {
        if (documento.length() == 8 && documento.charAt(documento.length() - 1) >= 'A' || documento.charAt(documento.length() - 1) <= 'Z' ||
                documento.charAt(documento.length() - 1) <= 'z' || documento.charAt(documento.length() - 1) >= 'a') {
            DNI = documento;
        } else {
            DNI = "000000000";
        }
    }
    public void setCuenta(String cuenta) {

        if (cuenta.length() == 24) {
            cuentas= cuenta;
        }
        else {
            cuentas = "000000000000000000000000";
        }
    }

    public void setSaldo() {
        saldo=0;
    }

    public void setnCuenta  () {
        Random genAle = new Random();
        String cta="";
        for (int i = 0; i < 24; i++) {
            cta+=genAle.nextInt(10);
        }
        nCuenta=cta;
    }

    //getters
    public String dameCuenta() {
        return cuentas;
    }
    public String



}
