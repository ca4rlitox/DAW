package ud8;

import java.util.Scanner;
import java.util.HashMap;

public class ejercicioEjemploDiccionario {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        HashMap<String, Integer> diccionario = new HashMap<>();
        String masRepetida="";
        int mayor=0;
        boolean opcion = true;

        do{
            System.out.println("Introduce la palabra a introducir en el diccionario:");
            String palabra = entrada.nextLine();
            if (palabra.equalsIgnoreCase("salir")) {
                opcion = false;
            }
            else if (diccionario.containsKey(palabra)){
                diccionario.put(palabra,diccionario.get(palabra)+1);
            }
            else {
                diccionario.put(palabra,1);
            }

        } while(opcion);

        for(String palabra: diccionario.keySet()){
            System.out.println("Palabra: "+palabra+". Numero de repeticiones: "+diccionario.get(palabra));
            int valor = diccionario.get(palabra);

            if (valor > mayor) {
            masRepetida = palabra;
            mayor = valor;
            }
        }
        System.out.println("\nLa palabra con más repeticiones es: ");
        System.out.println(masRepetida);





    }
}
