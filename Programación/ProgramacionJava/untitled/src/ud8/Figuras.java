package ud8;
// 1. Crear una clase abstracta Figura que contenga un atributo nombre y un
//m´eto do para obtener su nombre a s´ı como los m´eto dos abstractos: obtene-
//rArea y obtenerVolumen.
//2. De la clase anterior, heredan las siguientes clases (las cuales contienen los
//m´eto dos habituales y deb en sobreescribir los m´etod os que sean necesarios):
//Punto.
//Círculo.
//Cilindro (un cilindro se define por un punto, un radio y una altura.
//El ´area de un cilin dro es dos veces e l ´area de un c´ırculo m ´as 2 ∗ π ∗
//radio ∗ altura, y el volumen es π ∗ radio2 ∗ altura).
public abstract  class Figuras {
    private  String nombre;
    public Figuras(String nombre){
        this.nombre=nombre;
    }

    public String getNombre() {
        return nombre;
    }
    public abstract double calcularArea();
    public abstract double calcularVolumen();

    @Override
    public String toString() {
        return "Figuras{" +
                "nombre='" + nombre + '\'' +
                ", area=" + calcularArea() +" mº2"+
                ", volumen=" + calcularVolumen() +" mº3"+
                '}';
    }
}
