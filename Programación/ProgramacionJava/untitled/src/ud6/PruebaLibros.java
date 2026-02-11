package ud6;

import java.util.Scanner;

public class PruebaLibros {
    public static void main(String[] args) {
        Libro l = new Libro();
        ConjuntoLibros cl = new ConjuntoLibros();
        Scanner entrada = new Scanner(System.in);
        int opcion=0;
        String titulo;
        String autor;
        int calificacion;
        int numPags;

        do {
            System.out.println("1. Dar de alta libro");
            System.out.println("2. Eliminar libro");
            System.out.println("3. Obtener libro con mayor y menor calificacion");
            System.out.println("4. Ver todos los libros");
            System.out.println("5. Salir");
            opcion = entrada.nextInt();
            entrada.nextInt();
            switch (opcion) {
                case 1:
                    System.out.println("Dar alta libro.");
                    System.out.println("Introduce título: ");
                    titulo = entrada.nextLine();
                    System.out.println("Introduce autor: ");
                    autor = entrada.nextLine();
                    System.out.println("Introduce calificacion: ");
                    calificacion = entrada.nextInt();
                    System.out.println("Introduce el número de paginas: ");
                    numPags = entrada.nextInt();
                    cl.addLibro(new  Libro(titulo, autor, calificacion, numPags));
                    break;

                    case 2:
                        entrada.nextInt();
                        System.out.println("Eliminar libro:");
                        System.out.println("Opcion 1 para eliminar por título, 2 para eliminar por autor.");
                        opcion = entrada.nextInt();
                        if (opcion == 1) {
                            System.out.println("Introduce el nombre del título: ");
                            titulo = entrada.nextLine();
                            cl.eliminarLibros(titulo);
                        }
                        else if (opcion == 2) {
                            System.out.println("Introduce el nombre del autor: ");
                            autor = entrada.nextLine();
                            cl.eliminarLibros(autor);
                        }
                        else {
                            System.out.println("Opcion invalida. Intentalo de nuevo más tarde.");
                        }
                        break;
                case 3:
                    cl.mayorCalificacion();
                    break;
                case 4:
                    System.out.println("Todos los libros: "+cl);
                    break;
            }
        }while(opcion!=6);


    }
}
