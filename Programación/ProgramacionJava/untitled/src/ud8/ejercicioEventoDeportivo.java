package ud8;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;

public class ejercicioEventoDeportivo {
    public static void main(String[] args) {
        ArrayList<String> asistentes = new ArrayList<>();
        HashSet<String> asistentesUnicos = new HashSet<String>();
        HashSet<String> emailsDuplicados = new HashSet<>();
        Scanner entrada = new Scanner(System.in);
        String statement="";
        char opcion='S';

        do{
            System.out.println("Introdude el mail del asistente:");
            statement = entrada.nextLine();
            asistentes.add(statement);
            if (statement.equalsIgnoreCase("salir")) {
                opcion = 'N';
                asistentes.remove(statement);
            }
        } while (opcion != 'N');

        System.out.printf("Hay %d registros",asistentes.size());

        for (int i = 0; i < asistentes.size(); i++) {
            String palabra = asistentes.get(i);
            if (asistentes.indexOf(palabra) != asistentes.lastIndexOf(palabra)) {
                emailsDuplicados.add(palabra);
            }
            else {
                asistentesUnicos.add(palabra);
            }
        }

        System.out.printf("\nHay %d registros únicos%n",asistentesUnicos.size());
        System.out.println("Emails registros duplicados:");
        for (String email : emailsDuplicados) {
            System.out.println(email);
        }
        if (emailsDuplicados.isEmpty()) {
            System.out.println("No hay registros duplicados.");
        }




    }
}
