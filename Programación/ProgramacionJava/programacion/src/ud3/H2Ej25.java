package ud3;

public class H2Ej25 {
    public static void main(String[] args) {

        // Definimos variables
    int a=0;
    int b=1;
    int c=1;

    //0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
        //Establecemos contador para que pare cuando d valga 25

        for (int d=0;d<25;d++) {

            //Imprimimos el valor de a (al principio es 0)
            System.out.print(a +" ");

            // Guardamos en c el valor de a + b
            c = a + b;
            // Igualamos que a es lo mismo que b
            a = b;
            // Guardamos el valor de b para que sea el mismo que c y sea el numero que sume
            b = c;


        }

        }


    }

