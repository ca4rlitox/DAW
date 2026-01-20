package ud6;

public class Persona {
    private String nombre,dni;
    private char sexo;
    private int edad;
    private double altura,peso;

    public Persona (String nombre, String dni, int edad, double altura, double peso, char sexo) {
        this.nombre = nombre;
        this.dni = dni;
        this.edad = edad;
        this.altura = altura;
        this.peso = peso;
    }
    public Persona (String nombre, int edad,char sexo) {
        this.nombre = nombre;
        this.edad = edad;
        this.sexo = sexo;
        edad=0;
        dni="";
        altura=0;
        peso=0;

    }
}
