package ud3;

public class H2Ej18 {

	public static void main(String[] args) {
		// Que escriba las tablas de multiplicar del 0 al 10
		// Definimos variables
		int contadornumeros=-1;
		int resultado=0;
		int contadormultiplicador=0;
		
	while (contadormultiplicador <= 10) {
		contadornumeros= 0;
		System.out.println("\nTabla de multiplicar del "+contadormultiplicador+"\n");
		while (contadornumeros < 10) {

			resultado = contadornumeros * contadormultiplicador;
			contadornumeros++;
			System.out.println(contadormultiplicador+"x"+contadornumeros+"="+resultado);
		
			}
		contadormultiplicador= contadormultiplicador + 1;

		}
	}
	}

