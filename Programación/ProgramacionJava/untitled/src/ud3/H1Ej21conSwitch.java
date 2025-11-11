package ud3;

import java.util.Scanner;

public class H1Ej21conSwitch {
    public static void main(String[] args) {

        //Habilitamos la lectura de datos por consola
        Scanner entrada=new Scanner(System.in);
        //variables
        int opcion;
        double resultado;
        double lado;

        do {
            System.out.println("Para calcular el perímetro, selecciona que tipo de triángulo es (cm)");
            System.out.println("1. Equilatero");
            System.out.println("2. Isosceles");
            System.out.println("3. Escaleno");
            System.out.println("4. Salir");

            opcion = entrada.nextInt();
            switch (opcion) {

                case 1:
                    System.out.println("Introduce un lado de tu triángulo equilátero");
                    lado = entrada.nextDouble();

                    resultado = lado * 3;
                    System.out.println("El perímetro de tu triángulo es de "+resultado+" cm");
                    break;

                case 2:
                    System.out.println("Introduce el lado desigual de tu triángulo isósceles");
                    lado = entrada.nextDouble();
                    System.out.println("Introduce el lado igual de tu triángulo isósceles");
                    double ladoigual = entrada.nextDouble();

                    resultado = ladoigual * 2 + lado;
                    System.out.println("El perímetro de tu triángulo isósceles es de "+resultado+" cm");
                    break;

                case 3:
                    System.out.println("Introduce un lado de tu triángulo escaleno");
                    lado = entrada.nextDouble();
                    System.out.println("Introduce un lado de tu triángulo escaleno");
                    double lado1 = entrada.nextDouble();
                    System.out.println("Introduce un lado de tu triángulo escaleno");
                    double lado2 = entrada.nextDouble();

                    resultado = lado + lado1 + lado2;
                    System.out.println("El perímetro de tu triángulo es de "+resultado+" cm");
                    break;

                case 4:
                    System.out.println("Has salido.");
                    break;

                default:
                    System.out.println("Opción no válida. Inténtalo otra vez.");

            }
        } while (opcion >4 || opcion < 1);




    }
}
