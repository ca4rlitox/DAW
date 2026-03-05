package ud8;

public class Electrodomestico {
    private String color;
    private char consumoEnergetico;
    private double precioBase,peso;

    public Electrodomestico(String color, char consumoEnergetico, double precioBase, double peso) {
        setColor(color);
        setConsumoEnergetico(consumoEnergetico);
        this.precioBase = precioBase;
        this.peso = peso;
    }
    public Electrodomestico(double precioBase, double peso) {
        this("BLANCO",'F',precioBase,peso);
    }
    public Electrodomestico() {
        setColor("BLANCO");
        setConsumoEnergetico('F');
        setPrecioBase(100);
        setPeso(5);
    }

    public void setPrecioBase (double precioBase) {
        this.precioBase = precioBase;
    }
    public void setPeso (double peso) {
        this.peso = peso;
    }
    public void setColor (String color) {
        color = color.toUpperCase();
        if (color.equals("BLANCO") || color.equals("NEGRO") || color.equals("AZUL") || color.equals("ROJO") || color.equals("GRIS")) {
            this.color = color;
        }
        else {
            this.color = "BLANCO";
        }
    }
    public void setConsumoEnergetico (char consumoEnergetico) {
        String caracter = consumoEnergetico+"";
        caracter =  caracter.toUpperCase();
        consumoEnergetico = caracter.charAt(0);

        if (consumoEnergetico =='A' || consumoEnergetico == 'B' || consumoEnergetico == 'C' || consumoEnergetico == 'D'
                || consumoEnergetico == 'E' || consumoEnergetico == 'F') {
            this.consumoEnergetico = consumoEnergetico;
        }
        else {
            this.consumoEnergetico = 'F';
        }
    }
    public char getConsumoEnergetico() {
        return consumoEnergetico;
    }
    public String getColor() {
        return color;
    }
    public double getPrecioBase() {
        return precioBase;
    }
    public double getPeso() {
        return peso;
    }
    public boolean comprobarColor(char letra) {
        return letra >= 'A' && letra <= 'F';
    }
    public boolean comprobarColor(String color) {
        String[] colores = {"BLANCO", "NEGRO", "ROJO", "AZUL", "GRIS"};
        for (int i = 0; i < colores.length; i++) {
            if (color.equals(colores[i])) {
                return true;
            }
        }
        return false;
    }
    public double precioFinal() {
        double precioFinal=precioBase;
        //Sumamos al precio final segun el consumoEnergetico
        if (consumoEnergetico == 'A'){precioFinal+=100;}
        if (consumoEnergetico == 'B'){precioFinal+=80;}
        if (consumoEnergetico == 'C'){precioFinal+=60;}
        if (consumoEnergetico == 'D'){precioFinal+=50;}
        if (consumoEnergetico == 'E'){precioFinal+=30;}
        if (consumoEnergetico == 'F'){precioFinal+=10;}

        //Sumamos al precio final segun el peso
        if (peso >= 0 && peso < 20) {precioFinal+=10;}
        if (peso >= 20 && peso < 50) {precioFinal+=50;}
        if (peso >= 50 && peso < 80) {precioFinal+=80;}
        if (peso >= 80) {precioFinal+=100;}

        return precioFinal;
    }

    public String toString() {
        return "Color: "+this.color+" consumo energético: "+this.consumoEnergetico+" precio base: "+this.precioBase+
                "€ peso: "+this.peso+"kg";
    }
}
