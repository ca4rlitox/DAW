package ud6;

public class Persona {
    private String dni;
    private Cuenta[] cuentas;
    private int numCuentasAsociadas;
    public Persona(String dni){
        this.dni = dni;
        cuentas = new Cuenta[3];
        numCuentasAsociadas = 0;
    }
    //Setter
    public boolean addCuenta(Cuenta c) {
        if (numCuentasAsociadas>=3) {
            return false;
        }
        cuentas[numCuentasAsociadas] = c;
        numCuentasAsociadas++;
        return true;
    }
    public boolean esMorosa() {
        for (int i = 0; i < numCuentasAsociadas; i++) {
            if (cuentas[i].consultaSaldo()<0) {
                return true;
            }
        }
        return false;
    }
    //getter
    public String toString(){
        String cad="dni: "+dni+"\n"+"Cuentas: \n";
        for(int i=0; i<numCuentasAsociadas; i++){
            cad+=cuentas[i].toString();
        }
        return cad;
    }

    public String getDni() {
        return dni;
    }

    public Cuenta dameCuenta(String numC) {
        for (int i = 0; i < numCuentasAsociadas; i++) {
            if (cuentas[i].dameCuenta().equals(numC)) {
                return cuentas[i];
            }
        }
        return null;
    }
    public Cuenta dameCuentaMorosa() {
        for (int i = 0; i < numCuentasAsociadas; i++) {
            if (cuentas[i].consultaSaldo()<0) {
                return cuentas[i];
            }
        }
        return null;
    }
}
