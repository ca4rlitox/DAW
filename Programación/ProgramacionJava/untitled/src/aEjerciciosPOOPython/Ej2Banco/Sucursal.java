package aEjerciciosPOOPython.Ej2Banco;

public class Sucursal {
    private String direccion,provincia,cod_id;

    public Sucursal(String direccion, String provincia, String cod_id) {
        this.direccion = direccion;
        this.provincia = provincia;
        this.cod_id = cod_id;
    }

    public String getDireccion() {
        return direccion;
    }

    public String getProvincia() {
        return provincia;
    }

    public String getCod_id() {
        return cod_id;
    }
}
