package PracticaClinicaVeterinaria;

public class Reptil extends Animal {
    private String especie;
    private boolean venenoso;

    public Reptil (String nombre, String fechaNacimiento, double peso, String especie, boolean venenoso) {
        super(nombre, fechaNacimiento, "", peso);
        setEspecie(especie);
        this.venenoso = venenoso;
    }
    private void setEspecie(String especie) {
        if (especie.equalsIgnoreCase("Tortuga") || especie.equalsIgnoreCase("Iguana") || especie.equalsIgnoreCase("DragonDeComodo")) {
            this.especie = especie;
        }
        else{
            this.especie = null;
        }
    }
    public String dameDatosAnimal(){
        return "Ficha de reptil:\n" +
                "Nombre: "+ this.getNombre() +
                "\nEspecie: "+this.especie+
                "\nFecha de nacimiento: "+this.getFechaNacimiento()+
                "\nPeso: "+this.getPeso()+
                "\n¿Es venenoso?: "+this.venenoso+
                "\nComentarios: "+this.getComentarios();
    }
}
