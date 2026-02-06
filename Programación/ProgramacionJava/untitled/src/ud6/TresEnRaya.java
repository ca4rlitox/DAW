package ud6;

import java.util.Random;

public class TresEnRaya {
    private int jugador1;
    private int jugador2;
    private int movimientoRobotico;
    private int[][] tablero;
    private String fichas;

    public TresEnRaya() {
        this.jugador1 = 1;
        this.jugador2 = 2;
        this.movimientoRobotico = 0;
        this.tablero = new int[3][3];
    }

    public void mueveJugador1 (int pos) {

        if (pos == 1) {
            tablero[0][0] = 1;
        }
        if (pos == 2) {
            tablero[0][1] = 1;
        }
        if (pos == 3) {
            tablero[0][2] = 1;
        }
        if (pos == 4) {
            tablero[1][0] = 1;
        }
        if (pos == 5) {
            tablero[1][1] = 1;
        }
        if (pos == 6) {
            tablero[1][2] = 1;
        }
        if (pos == 7) {
            tablero[2][0] = 1;
        }
        if (pos == 8) {
            tablero[2][1] = 1;
        }
        if (pos == 9) {
            tablero[2][2] = 1;
        }
    }
    public void mueveJugador2 (int pos) {

        if (pos == 1) {
            tablero[0][0] = 2;
        }
        if (pos == 2) {
            tablero[0][1] = 2;
        }
        if (pos == 3) {
            tablero[0][2] = 2;
        }
        if (pos == 4) {
            tablero[1][0] = 2;
        }
        if (pos == 5) {
            tablero[1][1] = 2;
        }
        if (pos == 6) {
            tablero[1][2] = 2;
        }
        if (pos == 7) {
            tablero[2][0] = 2;
        }
        if (pos == 8) {
            tablero[2][1] = 2;
        }
        if (pos == 9) {
            tablero[2][2] = 2;
        }
    }

    public boolean movimientoValido(int pos) {
        int k=1;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++, k++) {
                if (pos == k && tablero[i][j] == 0) return true;
            }
        }
        return false;
    }
    public void mueveOrdenador1() {
        Random genAle = new Random();
        movimientoRobotico = genAle.nextInt(9)+1;
        if (!movimientoValido(movimientoRobotico)) {
            do {
                movimientoRobotico = genAle.nextInt(9) + 1;
            }while (!movimientoValido(movimientoRobotico));
        }
        mueveJugador1(movimientoRobotico);
    }
    public void mueveOrdenador2() {
        Random genAle = new Random();
        jugador2 = genAle.nextInt(9)+1;
        if (!movimientoValido(movimientoRobotico)) {
            do {
                movimientoRobotico = genAle.nextInt(9) + 1;
            }while (!movimientoValido(movimientoRobotico));
            mueveJugador2(movimientoRobotico);
        }
    }

    public void iniciar() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                tablero[i][j] = 0;
            }
        }
    }
    public void DibujaTablero() {
        System.out.println("-------------");
        for (int i = 0; i < 3; i++) {
            System.out.print("| " +circuloOequis(tablero[i][0])+ " | "+circuloOequis(tablero[i][1])+" | "+circuloOequis(tablero[i][2])+" | \n");
            System.out.println("-------------");
        }
    }

    public char circuloOequis (int num) {
        if (num == 1) return 'X';
        if (num == 2) return 'O';
        return ' ';
    }

    public boolean quedanMovimientos() {
        int ocupadas=0;
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    if (tablero[i][j] != 0) {
                        ocupadas++;
                    }
                }
        }
        return ocupadas < 9;
    }

    public boolean ganaJugador1() {
        for (int i = 0; i < 3; i++) {
            if (tablero[i][0] == jugador1 && tablero[i][1] == jugador1 && tablero[i][2] == jugador1) return true;
            if (tablero[0][i] == jugador1 && tablero[1][i] == jugador1 && tablero[2][i] == jugador1) return true;
        }
        if (tablero[0][0] == jugador1 && tablero[1][1] == jugador1 && tablero[2][2] == jugador1) return true;
        if (tablero[0][2] == jugador1 && tablero[1][1] == jugador1 && tablero[2][0] == jugador1) return true;
        return false;
    }

    public boolean ganaJugador2() {
        for (int i = 0; i < 3; i++) {
            if (tablero[i][0] == jugador2 && tablero[i][1] == jugador2 && tablero[i][2] == jugador2) return true;
            if (tablero[0][i] == jugador2 && tablero[1][i] == jugador2 && tablero[2][i] == jugador2) return true;
        }
        if (tablero[0][0] == jugador2 && tablero[1][1] == jugador2 && tablero[2][2] == jugador2) return true;
        if (tablero[0][2] == jugador2 && tablero[1][1] == jugador2 && tablero[2][0] == jugador2) return true;

        return false;
    }

}

