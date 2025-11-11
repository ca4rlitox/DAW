package ud3;

import java.util.Scanner;

public class H1Ej25 {

	public static void main(String[] args) {
		//Habilitamos la lectura de datos por consola
		Scanner entrada=new Scanner(System.in);
		
		System.out.println("Introduce la antigüedad en la empresa");
		//Leemos un entero
		int anos=entrada.nextInt();
		System.out.println("Introduce tu sueldo anual");
		//Leemos un decimal
		double sueldofijo=entrada.nextDouble();
		
		if (anos < 0) {
			System.out.println("Has introducido un valor negativo. Prueba otra vez poniendo otro positivo");
		}
		
		else if (anos > 10) {
			System.out.println("Tu sueldo es de "+sueldofijo*1.10);
		}
		
		else if (anos >= 5 && anos <= 10) {
			System.out.println("Tu sueldo es de "+sueldofijo*1.07);
		}
		
		else if (anos >= 3 && anos < 5) {
			System.out.println("Tu sueldo es de "+sueldofijo*1.05);
		}
		
		else if (anos < 3) {
			System.out.println("Tu sueldo es de "+sueldofijo*1.03);
		}
	
		
		
	}

}
