package ud8;

import java.util.ArrayList;

public class ConjuntoLibros {
    private ArrayList<Libro> productos;

    public ConjuntoLibros() {
        productos = new ArrayList<>();
    }

    public boolean addLibro (Libro l) {
        for (int i = 0; i < productos.size(); i++) {
            if (productos.get(i).getTitulo().equals(l.getTitulo())) {
                return false;
            }
            if (productos.get(i).getAutor().equals(l.getAutor())) {
                return false;
            }
        }
        productos.add(l);
        return true;
    }
    public boolean eliminarLibro(String tituloOautor) {
        for (int i = 0; i < productos.size(); i++) {
            if (productos.get(i).getTitulo().equals(tituloOautor)) {
                productos.remove(i);
                System.out.println("Libro eliminado");
                return true;
            }
            if (productos.get(i).getAutor().equals(tituloOautor)) {
                productos.remove(i);
                System.out.println("Libro eliminado");
                return true;
            }
        }
        System.out.println("Libro no eliminado bien porque no existe o se ha introducido de manera incorrecta el autor/título");
        return false;
    }
    public void mayorCalificacion() {
        int mayor=0;
        Libro libroConMayorCalificacion=null;
        for (int i = 0; i < productos.size(); i++) {
            if (productos.get(i).getCalificacion() > mayor) {
                mayor = productos.get(i).getCalificacion(); 
                libroConMayorCalificacion = productos.get(i);
            }
        }
        System.out.println("El libro con mayor calificación es:\n" + libroConMayorCalificacion);
    }
    public void menorCalificacion() {
        int menor=10;
        Libro libroConMenorCalificacion=null;
        for (int i = 0; i < productos.size(); i++) {
            if (productos.get(i).getCalificacion() < menor) {
                menor = productos.get(i).getCalificacion();
                libroConMenorCalificacion = productos.get(i);
            }
        }
        System.out.println("El libro con menor calificación es:\n"+libroConMenorCalificacion);
    }
    public String toString() {
        String cad="";
        if (productos.isEmpty()) {
            return "No hay nada que mostrar por ahora.";
        }

        for (int i = 0; i < productos.size(); i++) {
            cad+=productos.get(i).toString()+"\n";
        }
        return cad;
    }

}
