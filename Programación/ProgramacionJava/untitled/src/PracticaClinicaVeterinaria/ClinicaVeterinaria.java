package PracticaClinicaVeterinaria;

import java.util.ArrayList;

public class ClinicaVeterinaria {
    private ArrayList<Animal> animales;

    public ClinicaVeterinaria(){
        animales = new ArrayList<>();
    }

    public void insertaAnimal(Animal animal) {
        animales.add(animal);
    }
    public String buscaAnimal(String nombre) {

        for (int i = 0; i < animales.size(); i++) {
            if (animales.get(i).getNombre().equals(nombre)) {
            return animales.get(i).dameDatosAnimal();
            }
        }
        return null;
    }
    public boolean modificaComentarioAnimal(String animal, String comentario) {
        if (animales.isEmpty()) return false;
        Animal a=animales.get(0);
        for (int i = 0; i < animales.size(); i++) {
            if (animales.get(i).getNombre().equals(animal)) {
                a = animales.get(i);
            }
        }
        if (a == null) {
            return false;
        }
        a.setComentarios(comentario);
        return true;
    }
    public String toString() {
        String cad="";
        for(int i = 0; i < animales.size(); i++){
            cad+=animales.get(i).toString()+"\n";
        }
        return cad;
    }
}
