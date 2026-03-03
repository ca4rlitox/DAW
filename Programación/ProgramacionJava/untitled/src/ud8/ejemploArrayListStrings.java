package ud8;

import java.util.ArrayList;
import java.util.Scanner;

public class ejemploArrayListStrings {
    static Scanner entrada = new Scanner(System.in);
    public static void main(String[] args) {
        //Crear una lista de strings que almacene productos
        //Con un menu que contenga lo siguiente:
        //1. Añadir producto
        //2. Mostrar todos los productos
        //3. Borrar producto
        //4. Salir

        //Inicializamos la coleccion
        ArrayList<String> productos = new ArrayList<>();
        //Inicializamos cosas
        int opcion;

        do {
            mostrarMenu();
            opcion = entrada.nextInt();
            switch (opcion) {
                case 1:
                    productos.add(addProducto());
                    break;
                case 2:
                    mostrarProductos(productos);
                    break;
                case 3:
                    eliminarProductos(productos);
                    break;
                case 4:
                    System.out.println("Has salido.");
                    break;
                default:
                    System.out.println("Opción inválida. Intentalo otra vez.");
                    break;
            }
        }while (opcion!=4);
    }

    public static void mostrarMenu() {
        System.out.println("1. Añadir producto.");
        System.out.println("2. Mostrar todos los productos.");
        System.out.println("3. Borrar producto.");
        System.out.println("4. Salir.");
    }
    public static String addProducto() {
        entrada.nextLine();
        System.out.println("Introduce el producto que quieres añadir: ");
        return entrada.nextLine();
    }
    public static void mostrarProductos(ArrayList<String> productos) {
        for (int i = 0; i < productos.size(); i++) {
            System.out.println(i + 1+" - "+productos.get(i));
        }
        System.out.println();
    }
    public static void eliminarProductos(ArrayList<String> productos) {
        entrada.nextLine();
        System.out.println("Introduce el producto que quieres borrar: ");
        String productoAborrar = entrada.nextLine();
        if (!productos.contains(productoAborrar)) {
            System.out.println("El producto no existe, por lo que no se ha borrado.");
        }
        else {
            productos.remove(productoAborrar);
            System.out.println("Se ha borrado el producto correctamente.");
        }
        System.out.println();
    }
}
