package aEjerciciosPOOPython.Ej2Banco;

public class CuentaCorriente {
    private String cod_id,saldo,sucursal;

    public CuentaCorriente(String cod_id, String saldo, String sucursal) {
        setCod_id(cod_id);
        this.saldo = saldo;
        this.sucursal = sucursal;
    }

    private void setCod_id(String cod_id) {
        if (cod_id.length() == 4) {
            this.cod_id = "ES68 1234 "+cod_id;
        }
        else {
            this.cod_id = null;
        }
    }

    public String getCod_id() {
        return cod_id;
    }

    public String getSaldo() {
        return saldo;
    }

    public String getSucursal() {
        return sucursal;
    }
}
