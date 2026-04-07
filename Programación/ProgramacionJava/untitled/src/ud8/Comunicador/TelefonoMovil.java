package ud8.Comunicador;

public class TelefonoMovil extends Telefono implements Comunicador{
    private String SO;

    public TelefonoMovil(String marca, String tfn, String SO) {
        super(marca,tfn);
        this.SO = SO;
    }
    @Override
    public void enviarMensaje(String destinatario, String mensaje) {
        System.out.printf("Mensaje %s, destinatario: %s",mensaje,destinatario);
    }
    @Override
    public String toString() {
        return "\nMarca: "+super.getMarca()+" teléfono: "+super.getTfn()+" S.O "+this.SO;
    }
}
