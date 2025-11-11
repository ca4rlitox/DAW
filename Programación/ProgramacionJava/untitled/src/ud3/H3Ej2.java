package ud3;

import java.util.Scanner;

public class H3Ej2 {
    public static void main(String[] args) {
        //Habilitamos escaner
        Scanner sc = new Scanner(System.in);

       //Inicializamos variables
       int suma=0;
       int resultado;
       int i;
        //Pedimos número
        System.out.println("Introduce un número para saber si es perfecto");
        int num = sc.nextInt();

        for (i = 1;i<num;i++) {

            if (num % i == 0){
                suma = suma + i;
            }
        }
        if (suma == num) {
            System.out.println("Es un número perfecto");
        }
        else {
            System.out.println("El número no es perfecto");
        }




    }
}
