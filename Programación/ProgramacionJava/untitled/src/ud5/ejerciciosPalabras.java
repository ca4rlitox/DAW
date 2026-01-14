package ud5;

public class ejerciciosPalabras {
    public static void main(String[] args) {
        String cad = "hola a todes y adios a todes";
        String[] palabras = cad.split(" ");
        int[] estadisticas = new int[palabras.length];


        for (int i = 0; i < palabras.length; i++) {
            for (int j = 0; j < palabras.length; j++) {
                if (palabras[i].equals(palabras[j])) {
                    estadisticas[i]++;
                }
            }
        }

        for (int i = 0; i < palabras.length; i++) {
            System.out.println("La palabra "+palabras[i]+" aparece "+estadisticas[i]+" veces.");
        }
    }
}
