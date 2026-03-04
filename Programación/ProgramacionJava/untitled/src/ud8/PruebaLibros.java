package ud8;

import java.util.Scanner;

public class PruebaLibros {
    static Scanner entrada = new Scanner(System.in);
    static ConjuntoLibros cLibro = new ConjuntoLibros();
    static Libro l = new Libro();

    public static void main(String[] args) {
        int opcion;
        do {
            mostrarMenu();
            opcion = entrada.nextInt();
            switch (opcion) {
                case 1:
                    addLibro();
                    break;
                case 2:
                    borrarLibro();
                    break;
                case 3:
                    cLibro.mayorCalificacion();
                    break;
                case 4:
                    cLibro.menorCalificacion();
                    break;
                case 5:
                    System.out.println(cLibro);
                    break;
                default:
                    System.out.println("Opción inválida. Intentalo otra vez.");
                    break;
            }
        }while(opcion!=6);
    }
    public static void mostrarMenu() {
        System.out.println("1. Añadir libro");
        System.out.println("2. Borrar libro");
        System.out.println("3. Libro con mayor calificación");
        System.out.println("4. Libro con menor calificación");
        System.out.println("5. Mostrar todos los libros");
        System.out.println("6. Salir");
    }
    public static void addLibro() {
        entrada.nextLine();
        System.out.println("Introduce el nombre del libro a añadir: ");
        String nombre = entrada.nextLine();
        System.out.println("Introduce el autor del libro: ");
        String autor = entrada.nextLine();
        System.out.println("Introduce el número de paginas del libro: ");
        int numPags = entrada.nextInt();
        System.out.println("Introduce la calificación del libro (entre 0 y 10)");
        int calificacion = entrada.nextInt();
        if (calificacion < 0 || calificacion > 10) {
            do{
                System.out.println("No puede estar fuera de rango. Intentalo otra vez");
                System.out.println("Introduce la calificación del libro (entre 0 y 10)");
                calificacion = entrada.nextInt();
            }while(calificacion < 0 || calificacion > 10);
        }
        cLibro.addLibro(new Libro(nombre,autor,numPags,calificacion));
    }
    public static void borrarLibro() {
        entrada.nextLine();
        System.out.println("Introduce el titulo o el autor del libro a borrar: ");
        String titulo = entrada.nextLine();
        cLibro.eliminarLibro(titulo);
    }

}
