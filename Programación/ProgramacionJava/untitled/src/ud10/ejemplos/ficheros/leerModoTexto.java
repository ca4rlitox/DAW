package ud10.ejemplos.ficheros;

import java.io.FileReader;
import java.io.IOException;

public class leerModoTexto {
    public static void main (String[] args) {
        String cadenaFich="";
        FileReader entrada;
        int car=0;
        try {
            entrada = new FileReader("/home/alumno/Escritorio/fich.txt");
            while(car!=-1) {
                car = entrada.read();
                if (car != -1) {
                    cadenaFich+=(char)car;
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
