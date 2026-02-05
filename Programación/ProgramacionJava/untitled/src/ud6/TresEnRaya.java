package ud6;

import java.util.Random;

public class TresEnRaya {
    private int jugador1;
    private int jugador2;
    private int[][] tablero;
    private String fichas;

    public TresEnRaya() {
        this.jugador1 = jugador1;
        this.jugador2 = jugador2;
        this.fichas = fichas;
        this.tablero = new int[3][3];
        for (int i = 0; i < 3; i++) {
            tablero[i][0] = 0;
            tablero[0][i] = 0;
        }
    }

    public void mueveJugador1 (int pos) {

        if (pos > 9 || pos < 0) {
            System.out.println("Movimiento no válido");
        }
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
        if (pos > 9 || pos < 0) {
            return false;
        }
        if (tablero[0][0] == 0) {
            return true;
        }
        if (tablero[0][1] == 0) {
            return true;
        }
        if (tablero[0][2] == 0) {
            return true;
        }
        if (tablero[1][0] == 0) {
            return true;
        }
        if (tablero[1][1] == 0) {
            return true;
        }
        if (tablero[1][2] == 0) {
            return true;
        }
        if (tablero[2][0] == 0) {
            return true;
        }
        if (tablero[2][1] == 0) {
            return true;
        }
        if (tablero[2][2] == 0) {
            return true;
        }
        if (!quedanMovimientos()) {
            return false;
        }
        return false;
    }
    public void mueveOrdenador1() {
        Random genAle = new Random();
        jugador1 = genAle.nextInt(9)+1;
        if (!movimientoValido(jugador1)) {
            System.out.println("No se puede movimiento.");
        }
        else {
            mueveJugador1(jugador1);
        }
    }
    public void mueveOrdenador2() {
        Random genAle = new Random();
        jugador2 = genAle.nextInt(9)+1;
        if (!movimientoValido(jugador2)) {
            System.out.println("No se puede movimiento.");
        }
        else {
            mueveJugador1(jugador2);
        }
    }

    public void iniciar() {
        for (int i = 0; i < 3; i++) {
            tablero[i][0] = 0;
            tablero[0][i] = 0;
        }
    }
    public void DibujaTablero() {
        char equis = 'X';
        char circulo = 'O';
        char vacio = ' ';
        char pos0 = ' ';
        char pos1 = ' ';
        char pos2 = ' ';
        char pos3 = ' ';
        char pos4 = ' ';
        char pos5 = ' ';
        char pos6 = ' ';
        char pos7 = ' ';
        char pos8 = ' ';

        if (tablero[0][0] == 1) {
            pos1 = equis;
        } else if (tablero[0][0] == 2) {
            pos1 = circulo;
        } else {
            pos1 = vacio;
        }
        if (tablero[0][1] == 1) {
            pos2 = equis;
        } else if (tablero[0][1] == 2) {
            pos2 = circulo;
        } else {
            pos2 = vacio;
        }
        if (tablero[0][2] == 1) {
            pos3 = equis;
        } else if (tablero[0][2] == 2) {
            pos3 = circulo;
        } else {
            pos3 = vacio;
        }
        if (tablero[1][0] == 1) {
            pos4 = equis;
        } else if (tablero[1][0] == 2) {
            pos4 = circulo;
        } else {
            pos4 = vacio;
        }
        if (tablero[1][1] == 1) {
            pos5 = equis;
        } else if (tablero[1][1] == 2) {
            pos5 = circulo;
        } else {
            pos5 = vacio;
        }
        if (tablero[1][2] == 1) {
            pos6 = equis;
        } else if (tablero[1][2] == 2) {
            pos6 = circulo;
        } else {
            pos6 = vacio;
        }
        if (tablero[2][0] == 1) {
            pos7 = equis;
        } else if (tablero[2][0] == 2) {
            pos7 = circulo;
        } else {
            pos7 = vacio;
        }
        if (tablero[2][1] == 1) {
            pos8 = equis;
        } else if (tablero[2][1] == 2) {
            pos8 = circulo;
        } else {
            pos8 = vacio;
        }
        if (tablero[2][2] == 1) {
            pos0 = equis;
        } else if (tablero[2][2] == 2) {
            pos0 = circulo;
        } else {
            pos0 = vacio;
        }

        System.out.println("-------------\n" +
                "| " +pos1+ " | " + pos2 + " | " + pos3 + " | \n" +
                "-------------\n" +
                "| " + pos4 + " | " + pos5 + " | " + pos6 + " | \n" +
                "-------------\n" +
                "| " + pos7 + " | " + pos8 + " | " + pos0 + " | \n" +
                "-------------");


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
            if (ocupadas>=9) {
                return false;
            }
            return true;
    }

    public boolean ganaJugador1() {
        if (tablero[0][0] == 1 && tablero[1][1] == 1 && tablero[2][2] == 1) {
            return true;
        }
        if (tablero[0][0] == 1 && tablero[0][1] == 1 && tablero[0][2] == 1) {
            return true;
        }
        if (tablero[1][0] == 1 && tablero[1][1] == 1 && tablero[1][2] == 1) {
            return true;
        }
        if (tablero[2][0] == 1 && tablero[2][1] == 1 && tablero[2][2] == 1) {
            return true;
        }
        if (tablero[0][0] == 1 && tablero[1][0] == 1 && tablero[2][0] == 1) {
            return true;
        }
        if (tablero[0][1] == 1 && tablero[1][1] == 1 && tablero[2][1] == 1) {
            return true;
        }
        if (tablero[0][2] == 1 && tablero[1][2] == 1 && tablero[2][2] == 1) {
            return true;
        }
        if (tablero[0][2] == 1 && tablero[1][1] == 1 && tablero[2][0] == 1) {
            return true;
        }
        return false;
    }
    public boolean ganaJugador2() {
        if (tablero[0][0] == 2 && tablero[1][1] == 2 && tablero[2][2] == 2) {
            return true;
        }
        if (tablero[0][0] == 2 && tablero[0][1] == 2 && tablero[0][2] == 2) {
            return true;
        }
        if (tablero[1][0] == 2 && tablero[1][1] == 2 && tablero[1][2] == 2) {
            return true;
        }
        if (tablero[2][0] == 2 && tablero[2][1] == 2 && tablero[2][2] == 2) {
            return true;
        }
        if (tablero[0][0] == 2 && tablero[1][0] == 2 && tablero[2][0] == 2) {
            return true;
        }
        if (tablero[0][1] == 2 && tablero[1][1] == 2 && tablero[2][1] == 2) {
            return true;
        }
        if (tablero[0][2] == 2 && tablero[1][2] == 2 && tablero[2][2] == 2) {
            return true;
        }
        if (tablero[0][2] == 2 && tablero[1][1] == 2 && tablero[2][0] == 2) {
            return true;
        }
        return false;
    }

}

