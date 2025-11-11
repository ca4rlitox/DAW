package ud3;

import java.util.Scanner;

public class H2Ej16 {
    public static void main(String[] args) {

        // Inicializamos scanner
        Scanner sc = new Scanner(System.in);

        //Inicializamos contador
        int b = 0;

        //Pedimos numero (guardando el valor en a)
        System.out.println("Ingresa cuantos asteriscos quieres en pantalla");
        int a = sc.nextInt();

        //Usamos como contador b para que imprima hasta que sea como el numero introducido en a
        for (b = b; b < a; b++) {

            System.out.print("* ");

        }
    }
}