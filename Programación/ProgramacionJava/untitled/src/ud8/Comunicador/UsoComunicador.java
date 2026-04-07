package ud8.Comunicador;

public class UsoComunicador {
    public static void main (String[] args) {
        PalomaMensajera palomaAzul = new PalomaMensajera(true,"columbia livia","azul",'H',4);
        TelefonoMovil telefono1 = new TelefonoMovil("Apple","658404785","iOS");

        telefono1.enviarMensaje("684207501","he vuelto zorras");
        System.out.println(telefono1.toString());

    }
}
