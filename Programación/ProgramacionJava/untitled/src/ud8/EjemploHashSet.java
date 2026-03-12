package ud8;

import java.util.HashMap;
import java.util.HashSet;

public class EjemploHashSet {
    public static void main(String[] args) {
        HashSet<String> conjuntoFrutas = new HashSet<String>();

        //añado elementos al conjunto
        conjuntoFrutas.add("Kiwi");
        conjuntoFrutas.add("Plátano");
        conjuntoFrutas.add("Melón");
        conjuntoFrutas.add("Pera");

        for(String fruta : conjuntoFrutas){
            System.out.println(fruta);
        }

        System.out.println("Tamaño del conjunto: "+conjuntoFrutas.size());
        System.out.println("¿Está vacío? " +conjuntoFrutas.isEmpty());
        // Para vaciar el conjunto: conjuntoFrutas.clear()



    }


}
