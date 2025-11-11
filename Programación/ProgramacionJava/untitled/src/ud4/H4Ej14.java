package ud3;

import java.util.Scanner;

public class H4Ej14 {

    public static void main(String[] args) {
        //Definimos array
        final int TAM = 20;
        int[] nums = new int[200];
        int i = 0;
        //Habilitamos lectura por teclado
        Scanner entrada = new Scanner(System.in);

        //rellenamos el array
        for (i = 0; i < TAM; i++); {

            System.out.println("Introduce un número: ");
            nums[i] = entrada.nextInt();
        }
        System.out.println("Introduce el numero a buscar: ");
        int numAbuscar=entrada.nextInt();
        i=0;
        boolean numEncontrado=false;
        do {
            if (nums[i]==numAbuscar) {
                numEncontrado=true;
            }else {
                i++;
            }
        } while ((numAbuscar !=nums[i])&&(i<TAM));
        if (numEncontrado==true) {
            System.out.println("Valor encontrado en la posicion"+i);
        } else {
            System.out.println("Valor no encontrado");
        }
    }



}

