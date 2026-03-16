package ud9.Comunicador;

public class PalomaMensajera extends Paloma implements Comunicador{
    private int tiempoDeVuelo;

    public PalomaMensajera(boolean vuela, String especie, String color, char sexo, int tiempo) {
        super(vuela,especie,color,sexo);
        this.tiempoDeVuelo = tiempo;
    }

    public void setTiempoDeVuelo(int tiempoDeVuelo) {
        this.tiempoDeVuelo = tiempoDeVuelo;
    }
    public int getTiempoDeVuelo() {
        return this.tiempoDeVuelo;
    }

    public void enviarMensaje(String destinatario, String mensaje) {
        System.out.printf("Mensaje %s, destinatario: %s",mensaje,destinatario);
    }

    public String toString() {
        return "Tiempo de vuelo: "+this.tiempoDeVuelo;
    }
}
