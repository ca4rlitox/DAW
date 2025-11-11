package ud3;

public class H3Ej5deFibonacci {
    public static void main(String[] args) {
        int a=0, b=1, c=1, i=0;
        System.out.println("Vas a ver la sucesión de Fibonacci (los 10 primeros números");

        for (i = 1;i<15;i++) {

            System.out.println(a+" ");
            c = a + b;
            a = b;
            b = c;

        }



    }
}
