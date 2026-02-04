package ud6;

public class Notas {
    private String nombre;
    private double nota;

    public Notas(String nombre, double nota) {
        this.nombre = nombre;
        if (nota >= 0 && nota <= 10) {
            this.nota = nota;
        }
        else {
            nota=0;
        }
    }
    public Notas() {
        this.nombre = "";
        this.nota = 0;
    }

    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public double getNota() {
        return nota;
    }
    public void setNota(double nota) {
        if (nota >= 0 && nota <= 10) {
            this.nota = nota;
        }
        else {
            nota=0;
        }
    }

    public String toString() {
        return "Alumno: "+nombre+" con nota: "+nota;
    }
}
