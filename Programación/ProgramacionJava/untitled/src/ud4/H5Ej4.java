package ud4;

import java.util.Scanner;

public class H5Ej4 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.println("Introduce las dos notas");
        int x = entrada.nextInt();
        int y = entrada.nextInt();
        double media = media(x,y);
        System.out.println("La nota media es de "+media);


    }
    //cabecera
    public static double media(int a,int b) {

        //cuerpo
        double rsdo=(double)(a+b)/2;
        return rsdo;

    }
}
