package ud6;

public class ConjuntoLibros {

    static int TAM;
    private Libro[] conjuntoDeLibros;
    int espacioOcupado;

    public ConjuntoLibros() {
        TAM=10;
        conjuntoDeLibros = new Libro[TAM];
        espacioOcupado=0;
    }
    public boolean addLibro(Libro libro) {
        if (espacioOcupado==TAM) {
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

    public void mayorCalificacion () {
        int mayor=0;
        int menor=10;
        Libro mayorCali = null;
        Libro menorCali = null;
        for (int i = 0; i < espacioOcupado; i++) {
            if (conjuntoDeLibros[i].getCalificacion() > mayor) {
                mayorCali =  conjuntoDeLibros[i];
                mayor= conjuntoDeLibros[i].getCalificacion();
            }
        }
        for (int i = 0; i < espacioOcupado; i++) {
            if (conjuntoDeLibros[i].getCalificacion() < menor) {
                menorCali =  conjuntoDeLibros[i];
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
