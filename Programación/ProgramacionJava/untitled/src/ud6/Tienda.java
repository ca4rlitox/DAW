package ud6;

public class Tienda {

    private Productos[] productos;
    int espacioOcupado;

    public Tienda() {
        productos = new Productos[10];
        espacioOcupado = 0;
    }

    public boolean darAlta(Productos prod) {
        if (espacioOcupado == 10) {
            return false;
        }
        productos[espacioOcupado] = prod;
        espacioOcupado++;
        return true;
    }

    public Productos buscarProducto(String prod) {
        for (int i = 0; i < espacioOcupado; i++) {
            Productos p = productos[i];
            if (prod.equals(p.getNombre())) {
                return productos[i];
            }
        }
        return null;
    }

    public boolean modificarStock(String nombre,int stock, double precio) {
        for (int i = 0; i < espacioOcupado; i++) {
            Productos p = productos[i];
            if (p.getNombre().equals(nombre)) {
                productos[i].setStock(stock);
                productos[i].setPrecio(precio);
                return true;
            }
        }
        return false;
    }
    public String toString() {
        String cad="";
        for (int i = 0; i < espacioOcupado; i++) {
            cad+= productos[i].toString()+"\n";
        }
        return cad;
    }
}
