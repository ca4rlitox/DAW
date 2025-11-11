package ud3;

import java.util.Scanner;

public class H2Ej20conhacermientras {

	public static void main(String[] args) {
		// 20. Que haga un menú del tipo “desea salir (S/N)” y el programa no termine hasta que el usuario teclee “S”.
		
		//Habilitamos lectura por teclado
		char opcion='a';
		Scanner entrada=new Scanner(System.in);
		
		do {
			System.out.println("Desea salir? S/N");
			opcion=entrada.nextLine().charAt(0);
			
		}while (opcion != 's');

		System.out.println("Has salido fife");
		
	}

}
