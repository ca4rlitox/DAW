package ud3;

public class EjemploCondicional {

	public static void main(String[] args) {
		// Pedir un numero por teclado y ver si es positivo o negativo
			//Declaracion de variables
		//tipo nombreVariable son int = integral, double -> decimales, char -> chat, boolean -> true/false
	int num;
	
	// Mostrar "Introduce un número"
	System.out.println("Introduce un número");
	// Leer numero
	num=4;
	//si num > 0 entonces
	//Mostrar "El número es positivo"
	//Si no
	//Mostrar "El número es negativo"
	//fin_si
	
	if (num>0) {
		System.out.println("numero positivo");
	}
	else {
		
		System.out.println("número negativo");
	}
	}
}