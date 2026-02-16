package ud7;

public class Estudiantes extends Persona {
    private String curso;
    public Estudiantes (String nombre, String apellidos, String dni, String estadoCivil, String curso) {
        super(nombre,apellidos,dni,estadoCivil);
        this.curso = curso;
    }
    public String getCurso() {
        return curso;
    }
    public void setCurso(String curso) {
        this.curso = curso;
    }
    public String toString() {
        return super.toString()+" curso: "+curso;
    }
}
