package ud4;

public class EjemploFuncionSuma {
    public static void main (String[] args) {
        //lamo a la funcion
    int resultado=suma(2,3);
    System.out.println(resultado);
    resultado=suma(2,3);
    System.out.println(resultado);


    }

    //Paso 1, definimos la funcion
    //cabecera
    public static int suma(int a,int b) {
        //cuerpo
        int rsdo=a+b;
        return rsdo;


    }

}
