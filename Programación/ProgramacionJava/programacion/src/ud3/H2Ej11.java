package ud3;

import java.util.Scanner;

public class H2Ej11 {

	public static void main(String[] args) {
		//Habilitamos lectura por teclado
		Scanner entrada=new Scanner(System.in);
		// Definimos variables
		int entre=0;
		// 11. Que pida dos números y muestre todos los números que van desde el primero al segundo.
		// Se debe controlar que los valores son correctos.
		
		System.out.println("Indica el primer número para saber que numeros hay entre medias del siguiente que vas a introducir");
		int opcion1 = entrada.nextInt();
		System.out.println("Indica el segundo número");
		int opcion2 = entrada.nextInt();
		
		if (opcion1 < opcion2) do {
			
				System.out.println(opcion1+", "+opcion2);
				entre = opcion1 + 1;
				
			} while (entre != opcion2);
			
		if (opcion1 > opcion2) {

				entre = opcion2 + 1;
				System.out.println(opcion1+","+entre+","+opcion2);
			} while (opcion2 != opcion1);
		}
		


}
