package ud4;

public class ejemploRecursividad {

    public static void main(String[] args) {
        double num=52;
        System.out.println("El factorial de "+num+"  es "+factorial(num));

    }
    public static double factorial (double n) {

        if (n==0) { //caso base por definicion
            return 1;
        }
        else {      //caso general

            return n*factorial(n-1);

        }
    }
}
