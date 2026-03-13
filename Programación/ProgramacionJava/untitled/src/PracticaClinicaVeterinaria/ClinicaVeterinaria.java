package PracticaClinicaVeterinaria;

import java.util.ArrayList;

public class ClinicaVeterinaria {
    private ArrayList<Animal> animales;

    public ClinicaVeterinaria(){
        ArrayList<Animal> animals = new ArrayList<>();
    }

    public void insertaAnimal(Animal animal) {
        animales.add(animal);
    }
    public String buscaAnimal(String nombre) {

        for (Animal animal: animales) {
            if (animales.contains(animal)) {
                return animal.dameDatosAnimal();
            }
        }
        return null;
    }
}
