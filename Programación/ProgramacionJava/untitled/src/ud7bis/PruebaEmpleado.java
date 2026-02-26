package ud7bis;

import java.util.Scanner;

public class PruebaEmpleado {
    static Scanner entrada = new Scanner(System.in);
    public static void main(String[] args) {
        Empleado[] empleado = new Empleado[3];


        for (int i = 0; i < empleado.length; i++) {
            System.out.println("¿Qué tipo de empleado quieres dar de alta?");
            System.out.println("1.Base Mas Comision");
            System.out.println("2.PorComision");
            char opcion = entrada.nextLine().charAt(0);
            if (opcion == '1') {
                System.out.println("Introduce ");
            }
            else if (opcion == '2') {

            }
        }

    }
    public Empleado pedirDatosdeEmpleado(char opcion) {


        System.out.println("Introduce el nombre del empleado: ");
        String nombre = entrada.nextLine();
        System.out.println("Introduce el apellido del empleado: ");
        String apellido = entrada.nextLine();
        System.out.println("Introduce el numero de la seguridad social: ");
        String numSS = entrada.nextLine();
        System.out.println("Introduce el numero de ventas: ");
        String nVentas = entrada.nextLine();
        System.out.println("Introduce la comision por ventas en euros:");
        String comision = entrada.nextLine();
        if (opcion == '1') {
            System.out.println("Introduce el salario base: ");
            String salarioBase = entrada.nextLine();
            return new EmpleadoBaseMasComision(nombre, apellido, numSS, Integer.parseInt(salarioBase),Integer.parseInt(nVentas));
        }
        else if (opcion == '2') {
            System.out.println("Introduce la comision por ventas en euros:");
            System.out.println("Introduce ");
        }
        return null;
    }
}
