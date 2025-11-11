package ud3;

public class H2Ej4 {

	public static void main(String[] args) {
		// Que muestre los números pares que haya del 1 al 100.
		// Definimos las variables
		int par=0;
		
		while (par < 100) {
			par = par + 1;
			if (par % 2 == 0) {
				System.out.print(" "+par);
			}
		}
	}

}
