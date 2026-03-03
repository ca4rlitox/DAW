package ud8;

import java.util.ArrayList;

public class ejemploArrayList {
    public static void main (String[] args) {
        //Definimos coleccion
        ArrayList<Integer> numeros;
        //construimos la coleccion
        numeros = new ArrayList<>();
        System.out.println(numeros);
        numeros.add(1);
        numeros.add(2);
        numeros.add(0);

        System.out.println(numeros);
        //recorrer el array list
        for (int i = 0; i < numeros.size(); i++) {
            System.out.println(numeros.get(i));
        }
        //metodo para comprobar si hay un numero
        System.out.println(numeros.contains(1));
        //metodo para saber la posicion de un numero introducido
        System.out.println(numeros.indexOf(2));
        //para borrar toda la arraylist
        numeros.clear();
        System.out.println(numeros);
        //para borrar elemento de la arraylist por índice
        numeros.add(1); //elemento del índice 0
        numeros.add(1); //elemento del índice 1
        numeros.remove(1);

        //Crear una lista de strings que almacene productos
        //Con un menu que contenga lo siguiente:
        //1. Añadir producto
        //2. Mostrar todos los productos
        //3. Borrar producto
        //4. Salir
    }
}
