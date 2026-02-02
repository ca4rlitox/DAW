package ud6;

public class Cuenta {
    private String numCuenta;
    private  double saldo;
    public Cuenta(String numCuenta) {
        this.numCuenta = numCuenta;
        this.saldo = 0;
    }
    //Getter

    public String dameCuenta() {
        return numCuenta;
    }

    public double consultaSaldo() {
        return saldo;
    }

    //Setter
    public boolean recibirAbono(double cant) {
        if (cant>=0) {
            saldo+= cant;
            return true;
        }
        return false;
    }
    public boolean  pagarAbono(double cant) {
        if (cant>=0) {
            saldo-=cant;
            return true;
        }
        return false;
    }
    public String toString() {
        return "El Nº de cuenta es: "+numCuenta+"\nSaldo: "+saldo+"\n";
    }

}
