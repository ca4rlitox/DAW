package ud10.ExcepcionConjuntoLibro;

public class ConjuntoLibros {

    static int TAM;
    private Libro[] conjuntoDeLibros;
    int espacioOcupado;

    public ConjuntoLibros() {
        TAM=10;
        conjuntoDeLibros = new Libro[TAM];
        espacioOcupado=0;
    }
    public boolean addLibro(Libro libro) throws excepcionCalificacion {
        if (libro.getCalificacion() < 0 || libro.getCalificacion() > 10) {
            throw new excepcionCalificacion("Error. La calificacion debe estar entre 0 y 10.");
        }
        if (espacioOcupado==TAM) {
            return false;
        }
        if (existeLibro(libro)) {
            return false;
        }
        conjuntoDeLibros[espacioOcupado] = libro;
        espacioOcupado++;
        return true;
    }

    public boolean eliminarLibros(String nombre) {
        for (int i = 0; i < espacioOcupado; i++) {
            if (conjuntoDeLibros[i].getTitulo().equals(nombre)) {
                conjuntoDeLibros[i] = null;
                espacioOcupado--;
                return true;
            }
            if (conjuntoDeLibros[i].getAutor().equals(nombre)) {
                conjuntoDeLibros[i] = null;
                espacioOcupado--;
                return true;
            }
        }
        return false;
    }

    public boolean existeLibro(Libro l) {
        for (int i = 0; i < espacioOcupado; i++) {
            if (conjuntoDeLibros[i].getTitulo().equals(l.getTitulo())) {
                return true;
            }
        }
        return false;
    }

    public void mayorCalificacion () {
        int mayor=0;
        int menor=10;
        String mayorCali ="";
        String menorCali ="";
        for (int i = 0; i < espacioOcupado; i++) {
            if (conjuntoDeLibros[i].getCalificacion() > mayor) {
                mayorCali =  conjuntoDeLibros[i].getTitulo();
                mayor = conjuntoDeLibros[i].getCalificacion();
            }
        }
        for (int i = 0; i < espacioOcupado; i++) {
            if (conjuntoDeLibros[i].getCalificacion() < menor) {
                menorCali =  conjuntoDeLibros[i].getTitulo();
                menor = conjuntoDeLibros[i].getCalificacion();
            }
        }
        System.out.println("El libro con mayor calificacion es: "+mayorCali+" y el libro con menor calificacion es: "+menorCali);
    }

    public String toString() {
        String cad="";
        for (int i = 0; i < espacioOcupado; i++) {
            cad+=conjuntoDeLibros[i].toString();
        }
        return cad;
    }
}
