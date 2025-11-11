package ud3;

public class H1Ej2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// Definir variables
		int num;
		int num2;
		
		System.out.println("Introduce dos numeros enteros para determinar si son pares o impares");
		num=1;
		num2=1;
		
		while (num2==0) {
			System.out.println("Elige otro número");
		}
		while (num==0) {
			System.out.println("Elige otro número");
		}
		
		if ((num % 2 == 0) && (num2 % 2 == 0)) {
			System.out.println("Ambos números son pares");
		}			
		if ((num % 2 != 0) && (num2 % 2 != 0)) {
			System.out.println("Ambos números son impares");
		}
		if ((num % 2 != 0) && (num2 % 2 == 0)) {
			System.out.println("Hay un número impar y otro par");
		}
		if ((num % 2 == 0) && (num2 % 2 != 0)) {
			System.out.println("Hay un número impar y otro par");
		}
		
	}

}
