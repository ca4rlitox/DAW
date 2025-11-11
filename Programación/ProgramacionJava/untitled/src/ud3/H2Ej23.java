package ud3;

import java.util.Scanner;

public class H2Ej23 {

	public static void main(String[] args) {
		// Que solicite la media de X números, se dejarán de solicitar números hasta que se introduzca el cero.
		//Habilitamos la lectura por teclado
		Scanner entrada=new Scanner(System.in);
		//Definimos variables
		int cont=-1;
		double notas=0;
		int valor=-1;
		double media=0;
		
		while (valor != 0) {
			
			System.out.println("Escribe de uno en uno los números sobre los que quieres calcular la media, y presiona 0 para terminar.");
			valor = entrada.nextInt();
			notas = notas + valor;
			cont = cont + 1;
			
		}
		
		media = notas/cont;
		
		System.out.println("La media de las notas introducidas es "+media);

	}

}
