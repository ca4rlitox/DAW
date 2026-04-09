package ud10.ejemplos.excepciones;

public class ejemploExcepcion1 {

    //ejemplo de excepcion predefinida en Java
    public static double divide(double a, double b) throws ArithmeticException {
        if (b == 0) { //si el denominador es 0 lanzamos una excepcion
            throw new ArithmeticException("No se puede dividir entre 0 palurdo");
        }
    return a/b;

    }

    public static void main (String[] args) {
        try { //linea de codigo es susceptible de generar una excepcion
            System.out.println(divide(6, 0));
        } catch (ArithmeticException e) { // si se produce una excepcion entra en el catch, si no no
            System.out.println(e.getMessage());
        }
    }

}
