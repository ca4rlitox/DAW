package ud6;

public class Productos {
    private String nombre;
    private int stock;
    private double precio;

    public Productos(String nombre, int stock, double precio) {
        this.nombre = nombre;
        this.stock = stock;
        this.precio = precio;
    }

    public Productos() {
        this.nombre = "";
        this.stock = 0;
        this.precio = 0;
    }

    public String getNombre() {
        return nombre;
    }
    public String getStock() {
        return stock+"";
    }
    public double getPrecio() {
        return precio;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public void setStock(int nuevoStock) {
        this.stock = nuevoStock;
    }
    public void setPrecio(double precio) {
        this.precio = precio;
    }

    public String toString() {
        return "Nombre: " + nombre + ", Stock: " + stock + ", Precio: " + precio;
    }

}
