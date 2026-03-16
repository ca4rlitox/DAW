package ud9.Hablador;

public class Español extends Persona implements Hablador{

    public Español(String nombre, String apellidos) {
        super(nombre, apellidos);
    }
    public void Saluda() {
        System.out.println(getApellidos()+", "+getNombre()+" dice: Hola!");
    }
}
