package ud4;

public class H5Ej3 {
    public static void main (String[] args) {
        // Que muestre por pantalla los números del 1 al 100, utilizar recursividad.
        int num=1;

        System.out.println(recursividad(num));

    }

    public static int recursividad(int a) {

        if (a==100) {
            return 100;
        }
        else {
            System.out.print(a+" ");
            return recursividad(a + 1);
        }
    }
}
