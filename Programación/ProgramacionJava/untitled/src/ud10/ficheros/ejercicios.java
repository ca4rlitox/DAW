package ud10.ficheros;

import java.io.*;
import java.util.Random;
import java.util.Scanner;

public class ejercicios {
    static Scanner entrada = new Scanner(System.in);
    static Random genAle = new Random();
    public static void main (String[] args) {
        CopiaFicheroTexto();
    }

    public static void CopiaFicheroTexto() {
        System.out.println("Ejercicio 7: ");
        int caracter;
        try {
            System.out.println("Introduce el nombre del fichero a copiar: ");
            String nomFich = entrada.nextLine();
            FileReader lectura = new FileReader(nomFich);
            System.out.println("Introduce el nombre del fichero a crear: ");
            String fichCreado = entrada.nextLine();
            FileWriter escritura = new FileWriter(fichCreado);

            while((caracter = lectura.read()) != -1) {
                escritura.write(caracter);
            }

        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }

    public static void LeeFicheroTexto() {
        int caracter =0;
        System.out.println("Ejercicio 6: ");
        System.out.println("Indica el nombre del fichero");
        String nombreFichero = entrada.nextLine()+".txt";
        try (FileReader lector = new FileReader(nombreFichero)) {
            while ((caracter = lector.read()) != -1) {
                System.out.print((char)caracter);
     }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
    public static void EscribeFicheroTexto() {
        System.out.println("Ejercicio 5: ");
        System.out.println("Indica el nombre del fichero");
        String nombreFichero = entrada.nextLine();
        try (FileWriter escritura = new FileWriter(nombreFichero);) {
            System.out.println("Introduce la siguiente linea: ");
            String linea = entrada.nextLine();
            escritura.write(linea+"\n");
            while (!linea.isEmpty()) {
                System.out.println("Introduce la siguiente linea: ");
                linea = entrada.nextLine();
                if (!linea.isEmpty()) {
                    escritura.write(linea + "\n");
                }
                if (linea.isEmpty()) {
                    System.out.println("Terminado el ciclo.");
                }
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }

    public static void SumaFicheroInt() {
        int numLineas = 0;
        System.out.println("Ejercicio 4: ");
        System.out.println("Indica el nombre del fichero");
        String nombreFichero = entrada.nextLine();
        try (FileReader lectura = new FileReader(nombreFichero);) {
            // Primero contamos las lineas que tiene el fichero
            while (lectura.read() != -1) {
                if (lectura.read() != -1) {
                    numLineas++;
                }
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
        System.out.println(numLineas);
    }

    public static void EscribeFicheroNumRandom() {
        System.out.println("Ejercicio 3: ");
        System.out.println("Indica el nombre del fichero");
        String nombreFichero = entrada.nextLine();
        System.out.println("Indica el número de números aleatorios que quieres: ");
        int numLineas = entrada.nextInt();
        try (FileWriter fichero = new FileWriter(nombreFichero+".txt");) {
            for (int i = 0; i < numLineas; i++) {
                fichero.write(genAle.nextInt(100)+"\n");
            }
        }catch (IOException e) {
            System.out.println(e.getMessage());
        }


    }
    public void SumaFicheroInt10(String fichero) throws IOException {
        String contFichero="";
        for (int i = 0; i < 10; i++) {
            //genero el contenido del fichero
            contFichero+=genAle.nextInt(100)+"\n";
        }
        System.out.println(contFichero);
        try {
            FileWriter fichero1= new FileWriter(fichero);
            fichero1.close();
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }

    }
    public static void EscribeFicheroNumRandom10() {
        FileWriter escritura;
        System.out.println("Ejercicio 1");
        try {
            System.out.println("Indica el nombre del fichero a escribir");
            escritura = new FileWriter(entrada.nextLine());
            for (int i = 0; i < 10; i++) {
                escritura.write(genAle.nextInt()+"\n");
            }
            escritura.close();
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
        System.out.println("Fin ejercicio 1\n");
    }
}
