package ud4;

import java.util.Scanner;

public class EjemploVectoresArrays {
    public static void main(String[] args) {

        //Queremos guardar las notas de un alumno y calcular la media

        //Habilitamos entrada por teclado
        Scanner entrada=new Scanner(System.in);

        //Definimos un array de notas
        int [] notas;
        //Reservamos RAM para el array
        notas = new int[8];

        //Definimos variables
        double suma=0;
        double media=0;
        int i=0;

        for (i=0;i<8;i++) {

            System.out.println("Introduce nota "+(i+1)+":");
            notas[i]=entrada.nextInt();
            suma=suma+notas[i];
        }
        System.out.println("La media es de "+(suma/8));
        //mostramos las notas
        for (i=0;i<8;i++) {
            System.out.println("Nota: "+notas[i]);

        }



    }
}
