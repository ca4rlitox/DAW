package ud8;

public class Libro {
    private String titulo,autor;
    private int numPags,calificacion;

    public Libro(String titulo, String autor, int numPags, int calificacion) {
        this.titulo = titulo;
        this.autor = autor;
        this.numPags = numPags;
        setCalificacion(calificacion);
    }
    public Libro() {
        this.titulo = "";
        this.autor = "";
        this.numPags = 0;
        setCalificacion(0);
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public int getNumPags() {
        return numPags;
    }

    public void setNumPags(int numPags) {
        this.numPags = numPags;
    }

    public int getCalificacion() {
        return calificacion;
    }

    public void setCalificacion(int calificacion) {
        if (calificacion < 0 || calificacion > 10) {
            this.calificacion = 0;
        }
        else {
            this.calificacion = calificacion;
        }
    }
    public String toString(){
        return "Título: "+this.titulo+" Autor: "+this.autor+" Numero de páginas: "+this.numPags+" Calificacion: "+this.calificacion;
    }
}
