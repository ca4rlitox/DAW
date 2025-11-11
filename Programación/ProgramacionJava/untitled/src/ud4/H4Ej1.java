package ud4;

public class H4Ej1 {
    public static void main(String[] args) {

        //Que rellene un array con los 100 primeros número enteros y los muestre en pantalla en orden ASC

        //Constante
        final int TAM=5;
        //Definimos un array y reservamos ram para el array
        int [] numeros = new int[100];

        //Definimos variables
        int i=0;
        int num=0;
        //Guardamos los números en el array
        for (i=0;i<TAM;i++) {
            numeros[i]=num;
            num++;
        }
        //Mostramos array
        for (i=0;i<TAM;i++) {

            System.out.println(numeros[i]);

        }



    }
}
