package ud3;

import java.util.Scanner;

public class H1Ej21 {

	public static void main(String[] args) {
		// Que muestre un menú donde las opciones sean “Equilátero”, “Isósceles” y
		// “Escaleno”, pida una opción y calcule el perímetro del triángulo seleccionado.

		//Habilitamos la lectura de datos por consola
		Scanner entrada=new Scanner(System.in);
		//definimos variables
		int perimetro=0;
		// Solicitamos lo que se quiere hacer
		System.out.println("Para calcular el perímetro del triángulo selecciona: 1 para equilátero, 2 para isósceles y 3 para escaleno.");
		int opcion=entrada.nextInt();
		
		if ((opcion <= 0) || (opcion > 3)) {
			System.out.println("Opción introducida no válida. Inténtalo de nuevo.");
		}
		
		else if (opcion == 1) {
			System.out.println("Escribe el valor de un lado en centímetros");
			int lado=entrada.nextInt();
			perimetro=lado*3;
			System.out.println("El perímetro de tu triángulo es de "+perimetro+" cm.");
		}
		else if (opcion == 2) {
			System.out.println("Escribe cuanto miden los 2 lados iguales y luego del lado diferente (en centímetros)");
			int lado=entrada.nextInt();
			int lado1=entrada.nextInt();
			perimetro=(lado*2)+lado1;
			System.out.println("El perímetro de tu triángulo es de "+perimetro+" cm.");
		}
		else if (opcion == 3) {
			System.out.println("Escribe el valor de los 3 lados en centímetros.");
			int lado=entrada.nextInt();
			int lado1=entrada.nextInt();
			int lado2=entrada.nextInt();
			perimetro=(lado+lado1+lado2);
			System.out.println("El perímetro de tu triángulo es de "+perimetro+" cm.");
		}
		
		
	}

}
