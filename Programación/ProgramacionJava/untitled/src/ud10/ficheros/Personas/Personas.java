package ud10.ficheros.Personas;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class Personas {
    private ArrayList<Persona> personas;

    public Personas() {
        personas = new ArrayList<>();
    }

    public boolean addPersonas(Persona persona) {
        personas.add(persona);

        try (FileWriter escritura = new FileWriter("personas.txt")) {
            escritura.write(persona.getNombre()+", "+persona.getEdad()+"\n");
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
        return true;
    }
    public boolean quitarPersonas(Persona persona) {
        if (personas.contains(persona)) {
            return personas.remove(persona);
        }
        return false;
    }
    public String toString() {
        String cad="";
        for (Persona persona : personas) {
            cad+=persona;
        }
        return cad;
    }
}
