package ud8;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

public class ejemploHashMap {
    public static void main (String [] args) {
        HashMap<String, Integer> conjuntoFrutas = new HashMap<String, Integer>();

        // Para añadir PK-V
        conjuntoFrutas.put("Manzana", 5);
        conjuntoFrutas.put("Kiwi", 3);
        conjuntoFrutas.put("Albaricoque", 4);
        //Si se introduce otra clave con el mismo nombre, se sobreescribe el valor

        //Para obtener el valor de la clave, se utiliza .get (EJ: conjuntoFrutas.get("Manzana"))
        System.out.println(conjuntoFrutas.get("Manzana"));
        System.out.println("Número de frutas: "+conjuntoFrutas.size());
        System.out.println("¿Hay frutas? "+!conjuntoFrutas.isEmpty());

        //Para borrar un elemento se utiliza el .remove pasando la clave
        conjuntoFrutas.remove("Manzana");
        System.out.println("Número de frutas después del borrado de la manzana: "+conjuntoFrutas.size());

        Set <String> lista = conjuntoFrutas.keySet(); //Para sacar todos las claves

        System.out.println("\nElementos en el conjunto: ");
        for(String fruta: lista) {
            System.out.println(fruta);
        }

        //Comprobar si existe la clave .containsKey(clave)
        System.out.println("¿Existe el kiwi en el conjunto? "+conjuntoFrutas.containsKey("Kiwi"));
        //Comprobar si existe el valor .containsValue(valor)
        System.out.println(conjuntoFrutas.containsValue(1));
    }
}
