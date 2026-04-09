package ud10.ejemplos.excepciones;

public class usoEjemploExcepcion2 {

    public static void validarEdad (int edad) throws ejemploExcepcion2 {
        if ((edad <= 0) || (edad >= 100)) {
            throw new ejemploExcepcion2("Error, edad no está en rango. Debe estar entre 0 y 100");
        }
        else {
            System.out.println("Edad correcta.");
        }
    }
    public static void main (String[] args) throws ejemploExcepcion2 {
        try {
            validarEdad(300);
        } catch (ejemploExcepcion2 e) {
            System.out.println(e.getMessage());
        }
    }
}
