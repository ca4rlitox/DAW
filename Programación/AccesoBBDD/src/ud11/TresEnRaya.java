package ud11;

import java.util.Random;

public class TresEnRaya {
    private int[] tablero;

    public TresEnRaya() {
        this.tablero = new int[9];
    }

    public void mueveJugador1 (int pos) {
        if (movimientoValido(pos)) {
            tablero[pos-1] = 1;
        }
    }
    public void mueveJugador2 (int pos) {
        if (movimientoValido(pos)) {
            tablero[pos-1] = 2;
        }
    }
    public boolean movimientoValido(int pos) {
        // Si la posicion es menor que 1, mayor que 9 o en el tablero ya hay una cosa distinta de 0, devuelve false para que no salte outofbounds
        if (pos < 1 || pos > 9) {
            return false;
        }
        //Devolvemos true si no hay ficha donde nos piden.
        if (tablero[pos-1] == 0) {
            return true;
        }
        return false;
    }
    public void mueveOrdenador1() {
        Random genAle = new Random();
        int numAle = genAle.nextInt(9)+1;
        if (!movimientoValido(numAle)) {
            do {
                numAle = genAle.nextInt(9)+1;
            } while (!movimientoValido(numAle));
        }
        mueveJugador1(numAle);
    }
    public void mueveOrdenador2() {
        Random genAle = new Random();
        int numAle = genAle.nextInt(9)+1;
        if (!movimientoValido(numAle)) {
            do {
                numAle = genAle.nextInt(9)+1;
            } while (!movimientoValido(numAle));
        }
        mueveJugador2(numAle);
    }
    public void iniciar() {
        //Con esta funcion colocamos el valor de todas las casillas a 0.
        for (int i = 0; i < this.tablero.length; i++) {
            this.tablero[i] = 0;
        }
    }
    public void DibujaTablero() {
        System.out.println("-------------");
        for (int i = 0; i < tablero.length; i += 3) {
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
        //Aqui comprobamos si gana el 1 en las lineas horizontales
        if (tablero[0] == 1 && tablero[1] == 1 && tablero[2] == 1) return true;
        if (tablero[3] == 1 && tablero[4] == 1 && tablero[5] == 1) return true;
        if (tablero[6] == 1 && tablero[7] == 1 && tablero[8] == 1) return true;
        //Comprobamos lineas verticales
        if (tablero[0] == 1 && tablero[3] == 1 && tablero[6] == 1) return true;
        if (tablero[1] == 1 && tablero[4] == 1 && tablero[7] == 1) return true;
        if (tablero[2] == 1 && tablero[5] == 1 && tablero[8] == 1) return true;
        //Aqui comprobamos si gana el 1 en las diagonales
        if (tablero[2] == 1 && tablero[4] == 1 && tablero[6] == 1) return true;
        if (tablero[0] == 1 && tablero[4] == 1 && tablero[8] == 1) return true;

        return false;
    }
    public boolean ganaJugador2() {
        //Aqui comprobamos si gana el 2 en las lineas horizontales
        if (tablero[0] == 2 && tablero[1] == 2 && tablero[2] == 2) return true;
        if (tablero[3] == 2 && tablero[4] == 2 && tablero[5] == 2) return true;
        if (tablero[6] == 2 && tablero[7] == 2 && tablero[8] == 2) return true;
        //Aqui comprobamos si gana el 2 en las lineas verticales
        if (tablero[0] == 2 && tablero[3] == 2 && tablero[6] == 2) return true;
        if (tablero[1] == 2 && tablero[4] == 2 && tablero[7] == 2) return true;
        if (tablero[2] == 2 && tablero[5] == 2 && tablero[8] == 2) return true;
        //Aqui comprobamos si gana el 2 en las diagonales
        if (tablero[2] == 2 && tablero[4] == 2 && tablero[6] == 2) return true;
        if (tablero[0] == 2 && tablero[4] == 2 && tablero[8] == 2) return true;
        return false;
    }
    public String toString(){
        if (quedanMovimientos()) return "Quedan movimientos.";
        return "No quedan movimientos.";
    }

}