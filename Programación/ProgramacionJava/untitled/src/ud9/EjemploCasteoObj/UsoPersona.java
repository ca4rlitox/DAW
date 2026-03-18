package ud9.EjemploCasteoObj;

public class UsoPersona {
    public static void main(String[] args) {
        Persona p1 = new Persona("Pepe",40);
        Persona p2 = new Persona("Pepe",40);
        Persona p3 = new Persona("Pepe",50);

        if (p1.equals(p2)) {
            System.out.println("es la misma persona");
        }
        else {
            System.out.println("no es la misma persona.");
        }

        if (p2.equals(p3)) {
            System.out.println("es la misma persona");
        }
        else {
            System.out.println("no es la misma persona.");
        }

    }
}
