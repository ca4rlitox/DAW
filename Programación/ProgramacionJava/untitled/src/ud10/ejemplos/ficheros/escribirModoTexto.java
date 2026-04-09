package ud10.ejemplos.ficheros;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class escribirModoTexto {
    public static void main (String[] args) {
        // Defino el flujo o canal de salida
        FileWriter salida;

        try {
            //IOString (Creamos el canal)
            salida = new FileWriter("/home/alumno/Escritorio/fich.txt");
            for (int i = 0; i < 100000000; i++) {
                salida.write(i + "\n");
            }
            salida.close();
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}
