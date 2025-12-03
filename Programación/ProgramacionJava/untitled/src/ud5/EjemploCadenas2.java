package ud5;

public class EjemploCadenas2 {
    public static void main (String[] args) {

        String cad1="hola a todos";
        String cad2="HOLA";

        System.out.println(cad1.equals(cad2)); // compara strings, importandole las mayus/minus
        System.out.println(cad1.equalsIgnoreCase(cad2)); // compara strings sin importar mayus/minus
        System.out.println(cad1.indexOf('a')); //te mira la primera posicion del caracter introducido
        System.out.println(cad1.lastIndexOf('a')); //te mira la ultima posicion del caracter

        String[] palabras=cad1.split(" "); //te rellena un array de strings, separandolo en este caso por un espacio. ["holaa","a","todos"]

        for (int i =0;i< palabras.length;i++) {
            System.out.println(palabras[i]);
        }
    }
}
