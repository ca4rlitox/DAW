package ud6;

public class Persona {
    private String nombre,dni;
    private char sexo;
    private int edad;
    private double altura,peso;

    public Persona() {
        nombre="";
        sexo='H';
        edad=0;
        dni="";
        altura=0;
        peso=0;
    }

    public Persona (String nombre, int edad,char sexo) {
        this.nombre = nombre;
        this.sexo = sexo;
        this.edad = edad;
        dni="";
        altura=0;
        peso=0;

    }
    public Persona (String nombre, String dni, int edad, double altura, double peso, char sexo) {
        this.nombre = nombre;
        this.sexo = sexo;
        this.edad = edad;
        this.dni = dni;
        this.altura = altura;
        this.peso = peso;
    }

    public String setNombre(String nombre) {
        return nombre = nombre;
    }
    public String setSexo(char sexo) {
        if  (sexo=='M') return "M";
        if  (sexo=='m') return "M";
        if  (sexo=='F') return "F";
        if  (sexo=='f') return "F";
        return null;
    }

}
