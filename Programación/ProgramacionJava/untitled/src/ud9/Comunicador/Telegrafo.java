package ud9.Comunicador;

public class Telegrafo extends Reliquia implements Comunicador {
    private String codigo;

    public Telegrafo(int ano, String codigo) {
        super(ano);
        this.codigo = codigo;
    }

    public void enviarMensaje(String destinatario, String mensaje) {
        System.out.printf("Mensaje %s, destinatario: %s",mensaje,destinatario);
    }

    public String getCodigo() {
        return this.codigo;
    }
    public String toString() {
        return "Año: "+super.getAno()+this.codigo;
    }

}
