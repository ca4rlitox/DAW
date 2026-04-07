package ud8.Comunicador;

public interface Comunicador {
    //Una interfaz es un elemento en el que todos los métodos son abstractos.
    //***No tiene atributos***
    //Lo único que puede tener son constantes públicas y se convierte de manera implicita en public, static y final

    //La diferencia entre interfaz y abstraccion es, que algo es (clase abstracta) y lo que sabe hacer (la interfaz)
    void enviarMensaje(String destinatario, String mensaje);
}
