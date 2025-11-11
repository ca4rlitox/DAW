package ud3;

import java.util.Scanner;

public class H2Ej21
{
public static void main(String[] args)  {
    //Habilitamos el scanner
    Scanner sc = new Scanner(System.in);

    //Inicializamos variable

    int m=0;
    int a=1;

    //Solicitamos el número para calcular factorial
    System.out.println("Introduce el número para calcular su factorial");
    int f = sc.nextInt();

    //Hacemos un bucle con for para que mientras m no sea igual que f, siga haciendo a * m que es
    //como se calcula el factorial. El resultado se guarda en a.
    for (m=1;m<=f;m++) {

        a = a * m;

    }

    System.out.println(a);

}

}
