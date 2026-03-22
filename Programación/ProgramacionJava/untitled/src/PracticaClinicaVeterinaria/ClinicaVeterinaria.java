package PracticaClinicaVeterinaria;

import java.util.ArrayList;

public class ClinicaVeterinaria {
    private ArrayList<Animal> listaAnimales;

    public ClinicaVeterinaria(){
        listaAnimales = new ArrayList<>();
    }

    public void insertaAnimal(Animal animal) {
        listaAnimales.add(animal);
    }
    public Animal buscaAnimal(String nombre) {
        for (Animal listaAnimale : listaAnimales) {
            if (listaAnimale.getNombre().equals(nombre)) {
                return listaAnimale;
            }
        }
        return null;
    }
    public boolean modificaComentarioAnimal(String animal, String comentario) {
        if (listaAnimales.isEmpty()) return false;
        Animal a = buscaAnimal(animal);

        if (a == null) {
            return false;
        }
        a.setComentarios(comentario);
        return true;
    }
    public String toString() {
        String cad="";
        for (Animal listaAnimale : listaAnimales) {
            cad += listaAnimale.dameDatosAnimal()+"\n";
        }
        return cad;
    }
}
