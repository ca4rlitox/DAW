package PracticaCartaYbaraja;

import java.util.ArrayList;
import java.util.Collections;
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
            Collections.shuffle(lista_cartas);
        }
    }

    public void Barajar() {
        Collections.shuffle(lista_cartas);
    }
    public void Cortar(int posicion) {
        // Para cortar, hay que pasar la primera carta a la última posicion
        // y asi tantas veces como nos digan por parametro
        for (int i = 0; i < posicion; i++) {
            Carta cartaPrimera = lista_cartas.get(0);
            lista_cartas.remove(0);
            lista_cartas.add(cartaPrimera);
        }
    }
    public Carta Robar() {
        Carta cartaaDevolver = lista_cartas.get(0);
        lista_cartas.remove(0);
        return cartaaDevolver;
    }
    public void InsertaCartaFinal(int id_carta) {

    }

    public String toString() {
        return lista_cartas.toString();
    }
}
