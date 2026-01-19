package ud6;

public class Cuenta {
    //Atributos
    private String titular;
    private double cantidad;

    //Constructores
    public Cuenta (String tit) {
        titular = tit;
        cantidad = 0;
    }
    //2º Constructor
    public Cuenta (String tit, double cant) {
        titular = tit;
        cantidad = cant;
    }

    //Metodos setter
    public void setTitular(String nuevoTitular) {
        titular = nuevoTitular;
    }
    public void setCantidad(double nuevaCantidad) {
        cantidad = nuevaCantidad;
    }
    public void ingresar(double cantidadIngresada) {
        if (cantidadIngresada>0) {
            cantidad = cantidadIngresada+cantidad;
        }
    }

    public void retirar(double cantidadRetirada) {
        if (cantidadRetirada<cantidad) {
            cantidad=cantidad-cantidadRetirada;
        }else{
            cantidad=0;
        }
    }

    //getter
    public String getTitular() {
        return titular;
    }
    public double getCantidad() {
        return cantidad;
    }
    public String toString(){
        String cad="titular: "+getTitular()+" cantidad: "+getCantidad();
        return cad;
    }


}
