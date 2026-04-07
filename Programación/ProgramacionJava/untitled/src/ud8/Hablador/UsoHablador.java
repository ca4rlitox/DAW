package ud8.Hablador;

import java.util.ArrayList;

public class UsoHablador {
    public static void main (String[] args) {
        Español persona1 = new Español("Pepe","Luis");
        Gato firulais = new Gato();

        ArrayList<Hablador> saludos = new ArrayList<>();
        saludos.add(persona1);
        saludos.add(firulais);

        for (Hablador hablador : saludos){
            hablador.Saluda();
        }
    }
}
