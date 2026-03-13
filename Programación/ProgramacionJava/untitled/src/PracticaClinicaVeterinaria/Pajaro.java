package PracticaClinicaVeterinaria;

public class Pajaro extends Animal {
    private String especie;
    private boolean cantor;
    public Pajaro (String nombre, String fechaNacimiento, double peso, String especie, boolean cantor) {
        super(nombre, fechaNacimiento,"", peso);
        setEspecie(especie);
        this.cantor = cantor;
    }
    private void setEspecie(String especie) {
        if (especie.equalsIgnoreCase("Canario") || especie.equalsIgnoreCase("Periquito") ||
                especie.equalsIgnoreCase("Agapornis")) {
            this.especie = especie;
        }
        else{
            this.especie = null;
        }
    }

    public String dameDatosAnimal(){
        return "Ficha de pájaro:\n" +
                "Nombre: "+ this.getNombre() +
                "\nEspecie: "+this.especie+
                "\nFecha de nacimiento: "+this.getFechaNacimiento()+
                "\nPeso: "+this.getPeso()+
                "\n¿Es cantor?: "+this.cantor+
                "\nComentarios: "+this.getComentarios();
    }

}
