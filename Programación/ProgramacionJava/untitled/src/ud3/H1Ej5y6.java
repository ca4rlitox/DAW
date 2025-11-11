package ud3;

import java.util.Scanner;

public class H1Ej5y6 {

	public static void main(String[] args) {
		
		Scanner entrada=new Scanner(System.in);
		//Solicitamos los tres números y los leemos
		System.out.println("Introduce el primer número");
		int a=entrada.nextInt();
		
		System.out.println("Introduce el segundo número");
		int b=entrada.nextInt();

		System.out.println("Introduce el tercer número");
		int c=entrada.nextInt();
		
		// Hacemos al usuario elegir como lo quiere ordenar
		System.out.println("Si quieres ordenar de menor a mayor, escribe 1. Si quieres ordenar de mayor a menor, escribe 2.");
		int opcion=entrada.nextInt();
		
		
		if (opcion == 1 ) {
		//abc
		if (a < b & b < c) {
			System.out.println("Los números ordenados de menor a mayor es "+a+","+b+","+c);
		}
		//acb
		if (a < c & c < b) {
			System.out.println("Los números ordenados de menor a mayor es "+a+","+c+","+b);
		}
		//bac
		if (b < a & a < c) {
			System.out.println("Los números ordenados de menor a mayor es "+b+","+a+","+c);
		}
		//bca
		if (b < c & c < a) {
			System.out.println("Los números ordenados de menor a mayor es "+b+","+c+","+a);
		}
		//cab
		if (c < a & a < b) {
			System.out.println("Los números ordenados de menor a mayor es "+c+","+a+","+b);
		}
		//cba
		if (c < b & b < a) {
			System.out.println("Los números ordenados de menor a mayor es "+c+","+b+","+a);
		}
		
		}
		
		if (opcion == 2 ) {
		//abc
		if (a > b & b > c) {
			System.out.println("Los números ordenados de mayor a menor es "+a+","+b+","+c);
		}
		//acb
		if (a > c & c > b) {
			System.out.println("Los números ordenados de mayor a menor es "+a+","+c+","+b);
		}
		//bac
		if (b > a & a > c) {
			System.out.println("Los números ordenados de mayor a menor es "+b+","+a+","+c);
		}
		//bca
		if (b > c & c > a) {
			System.out.println("Los números ordenados de mayor a menor es "+b+","+c+","+a);
		}
		//cab
		if (c > a & a > b) {
			System.out.println("Los números ordenados de mayor a menor es "+c+","+a+","+b);
		}
		//cba
		if (c > b & b > a) {
			System.out.println("Los números ordenados de mayor a menor es "+c+","+b+","+a);
		}
		
		if ((opcion != 1) && (opcion != 2)) {
			System.out.println("Opción no válida. Intentalo de nuevo.");
		}
		}
	}

}
