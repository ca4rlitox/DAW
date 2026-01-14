package ud6;

public class Coche {

    //encapsulamos los atributos tributos
    private int ruedas;
    String motor,color,matricula;

    //Metodos
    public Coche (String nuevaMatricula) {
        int ruedas=4;
        matricula=nuevaMatricula;
    }

    //metodos getter: permiten leer el valor de un atributo desde fuera de la clase

    public int dameRuedas() {
        return ruedas;
    }

    //metodos setter: permiten modificar o escribir el valor de un atributo desde fuera de la clase

    public void estableceColor(String nuevoColor) {
        color=nuevoColor;
    }

    public String dameMatricula () {
        return matricula;
    }



    public void arrancar() {
        System.out.println("Has arrancado");
    }

    public void frenar() {
        System.out.println("Has frenado");
    }

    public void pitar() {
        System.out.println("Has pitado");
    }

}
