package ud3;

public class H2Ej10 {

	public static void main(String[] args) {
		// Que imprima la suma de todos los números impares que van del 1 al 100 y diga cuántos hay
		
		// Definimos variables
		int impar=0;
		int cont=0;
		
		while (impar < 100) {
			impar = impar + 1;
			if (impar % 2 != 0)
				System.out.println(impar);
			if (impar % 2 != 0)
				cont = cont + 1;
			
		}
		System.out.print("Hay "+cont+" impares");
	}

}
