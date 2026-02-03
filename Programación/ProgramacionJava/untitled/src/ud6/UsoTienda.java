package ud6;

import java.util.Scanner;

public class UsoTienda {
    public static void main(String[] args) {
        int opcion=0;
        Tienda t = new Tienda();
        Scanner sc = new Scanner(System.in);

        t.darAlta(new Productos("patatas ",1,1));
        t.darAlta(new Productos("patatas ",1,1));
        t.darAlta(new Productos("patatas ",1,1));
        t.darAlta(new Productos("patatas ",1,1));
        t.darAlta(new Productos("patatas ",1,2));

        System.out.println(t);

        t.modificarStock("patatas ",20,1);
        System.out.println(t);

        System.out.println(t.buscarProducto("patatas"));


    }
}
