package PracticaClinicaVeterinaria;

import java.util.ArrayList;
import java.util.Scanner;

public class UsoClinica {
    static Scanner entrada = new Scanner(System.in);
    public static void main (String[] args) {
        ArrayList<Animal> listaAnimales = new ArrayList<>();
        int opcion;

        do{
            muestraMenu();
            opcion = entrada.nextInt();
            switch (opcion) {
                case 1:
                    entrada.nextLine();
                    anadirAnimal(listaAnimales);

            }
        } while (opcion != 5);

    }
    public static void muestraMenu() {
        System.out.println("Bienvenido al sistema de gestión de la clínica veterinaria");
        System.out.println("1. Para añadir un animal.");
        System.out.println("2. Para buscar la ficha de un animal");
        System.out.println("3. Para añadir/modificar el comentario de un animal.");
        System.out.println("4. Para ver la ficha de todos los animales.");
    }

    public static ArrayList<Animal> anadirAnimal(ArrayList<Animal> listaAnimales) {
        System.out.println("Introduce el nombre del animal que quieres dar de alta: ");
        String especieAnimal = entrada.nextLine();
            while (!especieAnimal.equalsIgnoreCase("Perro") && !especieAnimal.equalsIgnoreCase("Gato") &&
                    !especieAnimal.equalsIgnoreCase("Reptil") && !especieAnimal.equalsIgnoreCase("Pajaro")) {
                System.out.println("Has introducido algo que no está contemplado. Escribe perro, gato, reptil o pajaro");
                especieAnimal = entrada.nextLine();
        }
        System.out.println("Introduce el nombre del "+especieAnimal+":");
        String nombreAnimal = entrada.nextLine();
        System.out.println("Introduce la fecha de nacimiento en formato DD/MM/YYYY");
        String fechaNacimiento = entrada.nextLine();
        System.out.println("Introduce el peso: ");
        entrada.nextLine();
        double pesoAnimal = entrada.nextDouble();
        System.out.println("¿Quieres introducir comentarios? (S/N)");
        char siNo = entrada.nextLine().charAt(0);
        if (siNo == 'S') {
            System.out.println("Introduce los comentarios: ");
            String comentariosAnimal = entrada.nextLine();
        }
        while (siNo != 'S' && siNo != 'N') {
            System.out.println("Opcion introducida inválida, intentalo otra vez.");
            System.out.println("¿Quieres introducir comentarios? (S/N)");
            siNo = entrada.nextLine().charAt(0);
            if (siNo == 'S') {
                String comentariosAnimal = entrada.nextLine();
            }
        }
        if (especieAnimal.equalsIgnoreCase("Perro") || especieAnimal.equalsIgnoreCase("Gato")) {
            System.out.println("Introduce el número de microchip: ");
            String microchipAnimal = entrada.nextLine();
            if (especieAnimal.equalsIgnoreCase("Perro")) {
                System.out.println("Introduce la raza: ");
                String razaAnimal = entrada.nextLine();
                while (!razaAnimal.equalsIgnoreCase("PastorAleman") && !razaAnimal.equalsIgnoreCase("Husky") &&
                        !razaAnimal.equalsIgnoreCase("FoxTerrier")) {
                    System.out.println("Raza no válida. Escribe de estas tres opciones: PastorAleman, Husky o FoxTerrier");
                    razaAnimal = entrada.nextLine();
                }

            } else if (especieAnimal.equalsIgnoreCase("Gato")) {
                System.out.println("Introduce la raza: ");
                String razaAnimal = entrada.nextLine();
                while (!razaAnimal.equalsIgnoreCase("Comun") && !razaAnimal.equalsIgnoreCase("Siames") &&
                        !razaAnimal.equalsIgnoreCase("Persa") && !razaAnimal.equalsIgnoreCase("Angora")
                        && !razaAnimal.equalsIgnoreCase("ScottishFold")) {
                    System.out.println("Raza no válida. Escribe de estas tres opciones: PastorAleman, Husky o FoxTerrier");
                    razaAnimal = entrada.nextLine();
                }
            }
        }
        if (especieAnimal.equalsIgnoreCase("Reptil") || especieAnimal.equalsIgnoreCase("Pajaro")) {
            System.out.println("Introduce la especie del animal:");
            if (especieAnimal.equalsIgnoreCase("Reptil")) {
                System.out.println("Introduce la especie: ");
                String especie = entrada.nextLine();
                while (!especie.equalsIgnoreCase("Tortuga") && !especie.equalsIgnoreCase("Iguana")
                        && !especie.equalsIgnoreCase("DragonDeComodo")) {
                    System.out.println("Raza no válida. Escribe de estas tres opciones: PastorAleman, Husky o FoxTerrier");
                    especie = entrada.nextLine();
                }
                System.out.println("¿Es cantarín?");
            }
        }

        return null;
        }



}
