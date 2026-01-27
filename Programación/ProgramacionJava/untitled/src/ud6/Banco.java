package ud6;

import java.util.Random;

public class Banco {
    private String DNI,numeroCuenta;
    private double saldo;
    private String[] cuentaBancaria = new String[3];


    public Banco() {

    }

    //setters
    public void setDNI (String documento) {
        DNI = documento;
    }
    public void setNumeroCuenta() {
        Random genAle = new Random();
        String numerodeCuenta="ES";
        for (int i = 0; i < 18; i++) {
            numerodeCuenta+=genAle.nextInt(10);
        }
        for (int i = 0; i < 3; i++) {
            if (cuentaBancaria[i].isEmpty()) {
                cuentaBancaria[i] = numerodeCuenta;
            }
        }
    }
    public void setSaldo (double saldoInicial) {
        saldo=saldoInicial;
    }
}
