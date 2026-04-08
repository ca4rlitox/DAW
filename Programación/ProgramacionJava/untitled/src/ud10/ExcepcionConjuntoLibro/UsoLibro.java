package ud10.ExcepcionConjuntoLibro;

public class UsoLibro {
    public static void main (String[] args) {
        ConjuntoLibros cL = new ConjuntoLibros();

        try {
            cL.addLibro(new Libro("Sancho panza", "quijote", 200, 500));
        } catch (excepcionCalificacion e) {
            System.out.println(e.getMessage());
        }
    }
}
