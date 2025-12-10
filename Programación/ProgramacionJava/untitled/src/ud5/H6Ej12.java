package ud5;

import java.util.Scanner;

public class H6Ej12 {
    static Scanner entrada = new Scanner(System.in);

    public static void main (String[] args) {

        //Realizar un programa en java que gestione los datos de stock de una
        //tienda de comestibles,la información a recoger será: nombre del producto(no se
        //puede repetir), precio, cantidad en stock.
        //La tienda dispone de 10 productos distintos. El programa debe ser capaz de:
        //1. Dar de alta un producto nuevo.
        //2. Buscar un producto por su nombre.
        //3. Modificar el stock y precio de un producto dado.

        //Habilitamos escaner
        Scanner entrada = new Scanner(System.in);

        //Habilitamos arrays

        String[] productos = new String [10];
        double[] precios =  new double [10];
        int[] stock = new int[10];
        int opcion=0;
        darAltaProducto(productos,precios,stock);


    }

    public static String[] darAltaProducto (String[] productos,double[] precios,int[] stock) {
        for (int i = 0;i<productos.length;i++) {

            if (productos[i] == null) {
                System.out.println("Introduce el nombre del producto que quieres introducir");
                productos[i] = entrada.nextLine();
                break;
            } else if (productos[i] != null) {
                System.out.println("Ya no quedan huecos para dar de alta productos. Máximo 10.");

            }
        }
            for (int i = 0;i<precios.length;i++) {
                if (precios[i] == 0.0) {
                    System.out.println("Introduce el precio del producto introducido.");
                    precios[i] = entrada.nextDouble();
                    break;
                } else if (precios[i] != 0.0) {
                    System.out.println("Ya no quedan huecos para dar de alta productos. Máximo 10.");
                }
            }
            for (int i = 0;i< stock.length;i++) {
                if (stock[i] == 0) {
                    System.out.println("Introduce el stock del producto introducido.");
                    stock[i] = entrada.nextInt();
                    break;
                } else if (stock[i] != 0) {
                    System.out.println("Ya no quedan huecos para dar de alta productos. Máximo 10.");
                }
            }
        System.out.println(productos[0]+" "+stock[0]+" "+precios[0]);

            return productos;
    }








public static void manu (String[] aa) {
        int opcion=3;
    do{
        switch (opcion) {
            case 1:
                System.out.println("Opción 1. Dar de alta un producto nuevo.");
            case 2:
                System.out.println("Opción 2. Buscar un producto por su nombre.");
                break;
            case 3:
                System.out.println("Opción 3. Modificar el stock y el precio de un producto.");
                break;
            default:
                System.out.println("Opción no válida");
        }
    } while (opcion!=4);
}

}
