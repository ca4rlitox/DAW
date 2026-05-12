package ud11;

import java.util.Random;

public class TresEnRaya {
    private int[] tablero;

    public TresEnRaya() {
        this.tablero = new int[9];
    }
    public void mueveJugador1 (int pos) {
        if (pos < 1 && pos > 9) {
            System.out.println("Movimiento inválido");
        }
        else if (tablero[pos-1] == 0) {
            tablero[pos] = 1;
        }
        else {
        }
    }
    public void mueveJugador2 (int pos) {
        if (pos < 1 && pos > 9) {
            System.out.println("Movimiento inválido");
        }
        else if (tablero[pos-1] == 0) {
            tablero[pos] = 1;
        }
        else {
        }
    }
    public boolean movimientoValido(int pos) {
        // Si la posicion es menor que 1, mayor que 9 o en el tablero ya hay una cosa distinta de 0, devuelve false
        if (pos < 1 && pos > 9 && tablero[pos-1] != 0) {
            return false;
        }
        //Devuelve true si el if no se cumple.
        return true;
    }
    public void mueveOrdenador1() {

    }
    public void mueveOrdenador2() {

    }
    public void iniciar() {
        //Con esta funcion colocamos el valor de todas las casillas a 0.
        for (int i = 0; i < this.tablero.length; i++) {
            this.tablero[i] = 0;
        }
    }
    public void DibujaTablero() {
        System.out.println("-------------");
        for (int i = 0; i < 9; i += 3) {
            System.out.print("| " + circuloOequis(tablero[i])+ " | " + circuloOequis(tablero[i+1]) + " | " + circuloOequis(tablero[i+2]) + " | \n");
            System.out.println("-------------");
        }
    }
    private char circuloOequis (int ficha) {
        //Con esta funcion devolvemos el caracter de la ficha
        if (ficha == 1) return 'X';
        if (ficha == 2) return 'O';
        return ' ';
    }
    public boolean quedanMovimientos() {
        for (int i = 0; i < tablero.length; i++) {
            // En el momento en el que haya una casilla libre, devuelve true
            if (tablero[i] == 0) {
                return true;
            }
        }
        // Si no ha devuelto true dentro del bucle, devuelve false.
        return false;
    }
    public boolean ganaJugador1() {
        //Aqui comprobamos si gana el 2 en las lineas verticales y horizontales
        for (int i = 0; i < 3; i++) {

        }
        //Aqui comprobamos si gana el 1 en las diagonales


        return false;
    }
    public boolean ganaJugador2() {
        //Aqui comprobamos si gana el 1 en las lineas verticales y horizontales
        for (int i = 0; i < 3; i++) {

        }
        //Aqui comprobamos si gana el 2 en las diagonales

        return false;
    }
    public String toString(){
        if (quedanMovimientos()) return "Quedan movimientos.";
        return "No quedan movimientos.";
    }

}