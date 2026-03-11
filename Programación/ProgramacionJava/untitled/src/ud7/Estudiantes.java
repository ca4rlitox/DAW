package ud7;

public class Estudiantes extends Persona {
    private String curso;
    public Estudiantes (String nombre, String apellidos, String estadoCivil, String curso) {
        super(nombre,apellidos,estadoCivil);
        this.curso = curso;
    }
    public String getCurso() {
        return curso;
    }
    public void setCurso(String curso) {
        this.curso = curso;
    }
    public void estoyAtendiendo(){
        System.out.println("Estoy de atendiendo");
    }
    public void estoyHablando() {
        System.out.println("Estoy hablando");
    }
    public String toString() {
        return super.toString()+" curso: "+curso;
    }
}
