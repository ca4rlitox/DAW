package ud3;

import java.util.Scanner;

public class H2Ej19 {

	public static void main(String[] args) {
		
		//Habilitamos lectura
		Scanner entrada=new Scanner(System.in);
		// Que muestre la tabla de multiplicar de un número cualquiera.
		int cont=0;
		int res=0;
		
		System.out.println("Escribe el número del cual quieres sacar la tabla de multiplicar.");
		int valor=entrada.nextInt();
		
		while (cont <= 10) {
			System.out.println(valor+" x "+cont+" = "+res);
			cont++;
			res = valor * cont;
		}
		
		

	}

}
