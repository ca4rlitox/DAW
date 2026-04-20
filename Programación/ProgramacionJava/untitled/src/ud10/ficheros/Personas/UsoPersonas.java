package ud10.ficheros.Personas;

import java.util.Scanner;

public class UsoPersonas {
    static Scanner entrada = new Scanner(System.in);
    public static void main (String[] args) {
        Personas personas = new Personas();
        int opcion;

        do {
            mostrarMenu();
            opcion = entrada.nextInt();
            switch (opcion) {
                case 1:
                    entrada.nextLine();
                    System.out.println("Introduce el nombre:");
                    String nombre = entrada.nextLine();
                    System.out.println("Introduce la edad: ");
                    int edad = entrada.nextInt();
                    if (personas.addPersonas(new Persona (nombre,edad))) {
                        System.out.println("Se ha añadido correctamente");
                    }
                    else {
                        System.out.println("Error.");
                    }
                    break;
                case 2:
                    break;
                case 3:
                    System.out.println(personas);
                    break;
                case 4:
                    System.out.println("Has salido");
                    break;
                default:
                    System.out.println("Opcion no válida. Intentalo de nuevo");
            }
        } while (opcion != 4);
    }

    public static void mostrarMenu() {
        System.out.println("1. Añadir persona");
        System.out.println("2. Eliminar persona");
        System.out.println("3. Mostrar personas.");
        System.out.println("4. Salir");
        System.out.print("Introduce una opcion: ");
    }
}
