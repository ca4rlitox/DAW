package ud6;

import java.util.Scanner;

public class UsoClase {
    public static void main(String[] args) {
        Clase c1 = new Clase();
        Notas n = new Notas();
        Scanner entrada = new Scanner(System.in);
        int opcion = 0;
        double nota=0;
        String alumno="";


        do{
            System.out.println("1. Para dar alta a un alumno");
            System.out.println("2. Para modificar la nota de un alumno");
            System.out.println("3. Para realizar la media de las notas y de todas las notas menores a 5");
            System.out.println("4. Para mostrar el alumno con mas nota y el alumno con menos nota");
            System.out.println("5. Para salir");
            opcion = entrada.nextInt();
            entrada.nextLine();
            switch(opcion){
                case 1:
                    System.out.println("Introduce el alumno a dar de alta: ");
                    alumno = entrada.nextLine();
                    System.out.println("Introduce la nota del alumno: ");
                    nota = entrada.nextDouble();
                    n = new Notas(alumno, nota);
                    System.out.println("Añadido correctamente.");
                    break;
                case 2:
                    entrada.nextInt();
                    System.out.println("Introduce el nombre del alumno el cual quieres modificar la nota:");
                    alumno = entrada.nextLine();
                    System.out.println("Introduce la nueva nota del alumno: ");
                    nota = entrada.nextDouble();
                    c1.modificarNota(alumno,nota);
                    if (!c1.modificarNota(alumno,nota)) {
                        System.out.println("No se ha modificado la nota.");
                    }
                    else {
                        System.out.println("Se ha modificado la nota.");
                    }
                    break;
                case 3:
                    System.out.println("La media de todos los alumnos es de: "+c1.realizarMedia()+"y\n" +
                            "de los alumnos que han sacado menos de un 5 es de: "+ c1.realizarMediaMenorA5());
                    break;
                case 4:
                    System.out.println("El alumno con mas nota es el siguiente:\n"+c1.alumnoConMasNota()+
                            "\n y el alumno con menos nota es el siguiente: \n"+c1.alumnoConMenosNota());
                    break;
                case 5:
                    System.out.println("Has salido.");

            }
        }while(opcion!=5);


    }
}
