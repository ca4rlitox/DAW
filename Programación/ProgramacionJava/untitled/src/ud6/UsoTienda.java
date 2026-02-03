package ud6;

import java.util.Scanner;

public class UsoTienda {
    public static void main(String[] args) {
        int opcion=0;
        Tienda t = new Tienda();
        Productos p = new Productos();
        Scanner sc = new Scanner(System.in);
        String nombre="";
        int stock = 0;
        double precio = 0;

        do {
            System.out.println("1. Dar de alta producto");
            System.out.println("2. Buscar un producto por su nombre.");
            System.out.println("3. Modificar el stock y precio de un producto dado.");
            System.out.println("4. Salir");
            opcion = sc.nextInt();
                switch (opcion) {
                    case 1:
                        sc.nextLine();
                        System.out.print("Introduce el nombre del producto: ");
                        nombre= sc.nextLine();
                        System.out.print("Introduce el stock: ");
                        stock = sc.nextInt();
                        System.out.print("Introduce el precio: ");
                        precio = sc.nextDouble();
                        t.darAlta(new Productos(nombre,stock,precio));
                        System.out.println("Producto dado de alta correctamente.\n"+t.toString());
                        break;
                    case 2:
                        sc.nextLine();
                        System.out.println("2. Buscar un producto por su nombre.");
                        nombre = sc.nextLine();
                        if (t.buscarProducto(nombre) == null) {
                            System.out.println("Producto no encontrado.");
                        }
                        else {
                            System.out.println(t.buscarProducto(nombre));
                        }
                        sc.nextLine();
                        break;
                    case 3:
                        sc.nextLine();
                        System.out.print("Introduce el nombre del producto el cual quieres modificar el stock/precio: ");
                        nombre = sc.nextLine();
                        System.out.print("Introduce el stock: ");
                        stock = sc.nextInt();
                        System.out.print("Introduce el precio: ");
                        precio = sc.nextDouble();
                        t.modificarStock(nombre,stock,precio);
                        sc.nextLine();
                        break;
                    case 4:
                        System.out.println("Has salido.");
                    default:
                        System.out.println("Opción no válida");
                }
                sc.nextLine();
        } while (opcion != 4);


    }
}
