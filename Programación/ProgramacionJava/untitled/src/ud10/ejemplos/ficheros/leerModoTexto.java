package ud10.ejemplos.ficheros;

import java.io.FileReader;
import java.io.IOException;

public class leerModoTexto {
    public static void main (String[] args) {
        String cadenaFich="";
        FileReader entrada;
        int fila=0;
        try {
            entrada = new FileReader("/home/alumno/Escritorio/fich.txt");
            while(fila!=-1) {
                fila = entrada.read();
                if (fila != -1) {
                    cadenaFich+=(char)fila;
                }
                System.out.println(cadenaFich);
            }
            entrada.close();
        }
        catch (IOException e) {
            System.out.println(e.getMessage());
        }

    }
}
