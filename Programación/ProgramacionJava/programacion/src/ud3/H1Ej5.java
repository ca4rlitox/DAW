package ud3;

import java.util.Scanner;

public class H1Ej5 {

	public static void main(String[] args) {
		// 5.Que pida 3 números y los muestre en pantalla de menor a mayor.
		//Habilitamos la lectura de datos por consola
		Scanner entrada=new Scanner(System.in);

		//Solicitamos los tres números y los leemos
		System.out.println("Introduce el primer número");
		int a=entrada.nextInt();
		
		System.out.println("Introduce el segundo número");
		int b=entrada.nextInt();

		System.out.println("Introduce el tercer número");
		int c=entrada.nextInt();
		
		// Ponemos las casuisticas
		
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

}
