package PracticaClinicaVeterinaria;

public class Perro extends Animal {
    private String raza,microchip;
    public Perro(String nombre, String fechaNacimiento, double peso, String raza, String microchip) {
        super(nombre,fechaNacimiento,peso);
        setRaza(raza);
        this.microchip = microchip;
    }

    public String getRaza() {
        return raza;
    }

    private void setRaza(String raza) {
        if (raza.equalsIgnoreCase("PastorAleman") || raza.equalsIgnoreCase("Husky") ||
        raza.equalsIgnoreCase("FoxTerrier")) {
            this.raza = raza;
        }
        else {
            this.raza = null;
        }
    }

    public String getMicrochip() {
        return microchip;
    }



    public String dameDatosAnimal() {
        return "Ficha de perro:\n" +
                "Nombre: "+ this.getNombre() +
                "\nRaza: "+this.raza+
                "\nFecha de nacimiento: "+this.getFechaNacimiento()+
                "\nPeso: "+this.getPeso()+
                "\nMicrochip: "+this.microchip+
                "\nComentarios: "+this.getComentarios();
    }
}
