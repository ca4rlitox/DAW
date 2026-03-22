package PracticaClinicaVeterinaria;

import java.util.ArrayList;
import java.util.Scanner;

public class UsoClinica {
    static Scanner entrada = new Scanner(System.in);
    static ClinicaVeterinaria cv = new ClinicaVeterinaria();
    public static void main (String[] args) {

        int opcion;
        do{
            muestraMenu();
            opcion = entrada.nextInt();
            switch (opcion) {
                case 1:
                    entrada.nextLine();
                    System.out.println("¿Que quieres añadir?\n" +
                            "1. Para perro\n" +
                            "2. Para gato\n" +
                            "3. Para reptil\n" +
                            "4. Para pajaro");
                    addAnimal(entrada.nextInt());
                    break;
                case 2:
                    mostrarFicha();
                    break;
                case 3:
                    modificarComentario();
                    break;
                case 4:
                    System.out.println(cv);
                    break;
                default:
                    System.out.println("Opción inválida. Intentalo de nuevo.");
            }
        } while (opcion != 5);
        System.out.println("Has salido correctamente.");
    }
    public static void muestraMenu() {
        System.out.println("Bienvenido al sistema de gestión de la clínica veterinaria");
        System.out.println("1. Para añadir un animal.");
        System.out.println("2. Para buscar la ficha de un animal");
        System.out.println("3. Para añadir/modificar el comentario de un animal.");
        System.out.println("4. Para ver la ficha de todos los animales.");
    }

    public static void addAnimal(int opcion) {
        entrada.nextLine();
        if (opcion < 1 || opcion > 4) {
            while (opcion < 1 || opcion > 4) {
                System.out.println("Opcion introducida inválida. Inténtalo otra vez.");
                opcion = entrada.nextInt();
            }
        }
        System.out.println("Introduce el nombre del animal:");
        String nombreAnimal = entrada.nextLine();
        System.out.println("Introduce la fecha de nacimiento: ");
        String fechaNacimientoAnimal = entrada.nextLine();
        System.out.println("Introduce el peso del animal: ");
        double pesoAnimal = entrada.nextDouble();
        if (opcion == 1 || opcion == 2) {
            entrada.nextLine();
            System.out.println("Introduce la raza: ");
            String razaAnimal = entrada.nextLine();
            System.out.println("Introduce el microchip: ");
            String microchipAnimal = entrada.nextLine();
            if (opcion == 1) {
                cv.insertaAnimal(new Perro(nombreAnimal, fechaNacimientoAnimal, pesoAnimal, razaAnimal, microchipAnimal));
            } else {
                cv.insertaAnimal(new Gato(nombreAnimal, fechaNacimientoAnimal, pesoAnimal, razaAnimal, microchipAnimal));
            }
        }
            if (opcion == 3) {
                boolean venenoso = false;
                System.out.println("Introduce la especie: ");
                String especieAnimal = entrada.nextLine();
                System.out.println("¿Es venenoso? Escribe una S para indicar que si, cualquier otra letra para indicar que no.");
                char venenosoAnimal = entrada.nextLine().charAt(0);
                if (venenosoAnimal == 'S') {
                    venenoso = true;
                }
                cv.insertaAnimal(new Reptil(nombreAnimal, fechaNacimientoAnimal, pesoAnimal, especieAnimal, venenoso));
            }

        if (opcion == 4) {
            boolean cantarin = false;
            System.out.println("Introduce la especie: ");
            String especieAnimal = entrada.nextLine();
            System.out.println("¿Es cantarin? Escribe una S para indicar que si, cualquier otra letra para indicar que no.");
            char cantarinAnimal = entrada.nextLine().charAt(0);
            if (cantarinAnimal == 'S') {
                cantarin = true;
            }
            cv.insertaAnimal(new Pajaro(nombreAnimal, fechaNacimientoAnimal, pesoAnimal, especieAnimal, cantarin));
        }
    }
    public static void mostrarFicha() {
        entrada.nextLine();
        System.out.println("Introduce el nombre del animal: ");
        String busquedaAnimal = entrada.nextLine();
        if (cv.buscaAnimal(busquedaAnimal) == null) {
            System.out.println("Ese animal no existe.");
        }
        else {
            System.out.println(cv.buscaAnimal(busquedaAnimal).dameDatosAnimal());
        }
    }
    public static void modificarComentario() {
        entrada.nextLine();
        System.out.println("Introduce el nombre del animal al que quieres poner/cambiar el comentario: ");
        String nomAnimal = entrada.nextLine();
        System.out.println("Introduce el comentario a continuación: ");
        String comentAnimal = entrada.nextLine();
        if (cv.modificaComentarioAnimal(nomAnimal,comentAnimal)) {
            System.out.println("Se ha modificado el comentario.");
        }else {
            System.out.println("No se ha modificado el comentario.");
        }
    }

}

