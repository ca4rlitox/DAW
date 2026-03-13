package PracticaClinicaVeterinaria;

public class Gato extends Animal {
    private String raza,microchip;

    public Gato (String nombre, String fechaNacimiento, double peso, String raza, String microchip) {
        super(nombre,fechaNacimiento,"",peso);
        setRaza(raza);
        this.microchip = microchip;
    }

    public String dameDatosAnimal(){
        return "Ficha de perro:\n" +
                "Nombre: "+ this.getNombre() +
                "\nRaza: "+this.raza+
                "\nFecha de nacimiento: "+this.getFechaNacimiento()+
                "\nPeso: "+this.getPeso()+
                "\nMicrochip: "+this.microchip+
                "\nComentarios: "+this.getComentarios();
    }

    private void setRaza(String raza) {
        if (raza.equalsIgnoreCase("Comun") || raza.equalsIgnoreCase("Siames") ||
                raza.equalsIgnoreCase("Persa") || raza.equalsIgnoreCase("Angora")
                || raza.equalsIgnoreCase("ScottishFold")) {
            this.raza = raza;
        }
        else {
            this.raza = null;
        }
    }
    public String getRaza() {
        return raza;
    }

    public String getMicrochip() {
        return microchip;
    }
}