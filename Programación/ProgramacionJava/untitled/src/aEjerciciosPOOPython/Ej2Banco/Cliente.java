package aEjerciciosPOOPython.Ej2Banco;

public class Cliente {
    private String nombre,apellidos,nif,telefono,sucursal;
    public Cliente(String nombre, String apellidos, String nif, String telefono, String sucursal) {
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.nif = nif;
        this.telefono = telefono;
        this.sucursal = sucursal;
    }
    public String getSucursal() {
        return sucursal;
    }
}
