package PracticaCartaYbaraja;

import java.util.ArrayList;
import java.util.Random;

public class Baraja {
    private ArrayList<Carta> lista_cartas;

    public Baraja() {
        Random genAle = new Random();
        lista_cartas = new ArrayList<>();

        for (int i = 0; i < 40; i++) {
            int numAle = (genAle.nextInt(39)+1);
            lista_cartas.add(new Carta(numAle));
        }
    }
    public Baraja(int tipoBaraja) {
        Random genAle = new Random();
        lista_cartas = new ArrayList<>();

        if (tipoBaraja == 1) {
            for (int i = 0; i < 40; i++) {
                int numAle = (genAle.nextInt(39)+1);
                lista_cartas.add(new Carta(numAle));
            }
        }
        if (tipoBaraja == 2) {
            for (int i = 0; i < 80; i++) {
                int numAle = (genAle.nextInt(39)+1);
                lista_cartas.add(new Carta(numAle));
            }
        }
    }
    public Baraja(int tipoBaraja, boolean barajar) {
        Random genAle = new Random();
        lista_cartas = new ArrayList<>();

        if (tipoBaraja == 1) {
            for (int i = 0; i < 40; i++) {
                int numAle = (genAle.nextInt(39)+1);
                lista_cartas.add(new Carta(numAle));
            }
        }
        if (tipoBaraja == 2) {
            for (int i = 0; i < 80; i++) {
                int numAle = (genAle.nextInt(39)+1);
                lista_cartas.add(new Carta(numAle));
            }
        }
        if (barajar) {
            ArrayList <Carta> otraListadeCartas = new ArrayList<>();
            otraListadeCartas = lista_cartas;
            for (int i = 0; i < 40; i++) {
                otraListadeCartas.add(lista_cartas.get(i));
            }
            do {
                int numAle = genAle.nextInt(39)+1;
                int carta = otraListadeCartas.get(numAle).getNumero();
                lista_cartas.add(new Carta(carta));
                otraListadeCartas.remove(carta);
            }while(!otraListadeCartas.isEmpty());
        }
    }

    public String toString() {
        return lista_cartas.toString();
    }
}
