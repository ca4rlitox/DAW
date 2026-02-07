package ud6;

import java.util.Random;

public class TresEnRaya {
    private int jugador1,jugador2,robot1,robot2;
    private int[][] tablero;

    public TresEnRaya() {
        this.jugador1 = 1;
        this.jugador2 = 2;
        this.robot1 = 1;
        this.robot2 = 2;
        this.tablero = new int[3][3];
    }
    public void mueveJugador1 (int pos) {
        int contador = 1;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++, contador++) {
                if (pos == contador) {
                    tablero[i][j] = jugador1;
                }
            }
        }
    }
    public void mueveJugador2 (int pos) {
        int contador = 1;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++, contador++) {
                if (pos == contador) {
                    tablero[i][j] = jugador2;
                }
            }
        }
    }
    public boolean movimientoValido(int pos) {
        int contador = 1;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++, contador++) {
                if (pos == contador && tablero[i][j] == 0) return true;
            }
        }
        return false;
    }
    public void mueveOrdenador1() {
        int contador = 1;
        int pos;
        Random genAle = new Random();
        pos = genAle.nextInt(9)+1;
        if (!movimientoValido(pos)) {
            do {
                pos = genAle.nextInt(9) + 1;
            }while (!movimientoValido(pos));
        }
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++,contador++) {
                if (pos == contador) {
                    tablero[i][j] = robot1;
                }
            }
        }
    }
    public void mueveOrdenador2() {
        int contador=1;
        int pos;
        Random genAle = new Random();
        pos = genAle.nextInt(9)+1;
        if (!movimientoValido(pos)) {
            do {
                pos = genAle.nextInt(9) + 1;
            }while (!movimientoValido(pos));
        }

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++,contador++) {
                if (pos == contador) {
                    tablero[i][j] = robot2;
                }
            }
        }
    }
    public void iniciar() {
        //Con esta funcion colocamos el valor de todas las casillas a 0.
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                tablero[i][j] = 0;
            }
        }
    }
    public void DibujaTablero() {

        //Con un bucle dibujamos el tablero
        System.out.println("-------------");
        for (int i = 0; i < 3; i++) {
            System.out.print("| " +circuloOequis(tablero[i][0])+ " | "+circuloOequis(tablero[i][1])+" | "+circuloOequis(tablero[i][2])+" | \n");
            System.out.println("-------------");
        }
    }
    public char circuloOequis (int ficha) {
        //Con esta funcion devolvemos el caracter de la ficha
        if (ficha == 1) return 'X';
        if (ficha == 2) return 'O';
        return ' ';
    }
    public boolean quedanMovimientos() {
        int ocupadas=0;
        //Hacemos un bucle para recorrer el tablero y ver si están las casillas ocupadas.
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    if (tablero[i][j] != 0) {
                        ocupadas++;
                    }
                }
        }
        //Devuelve true si hay menos de 9 fichas colocadas.
            return ocupadas < 9;
    }
    public boolean ganaJugador1() {
        //Aqui comprobamos si gana el jugador1 o el robot1
        for (int i = 0; i < 3; i++) {
            if (tablero[i][0] == 1 && tablero[i][1] == 1 && tablero[i][2] == 1) return true;
            if (tablero[0][i] == 1 && tablero[1][i] == 1 && tablero[2][i] == 1) return true;
        }
        if (tablero[0][0] == 1 && tablero[1][1] == 1 && tablero[2][2] == 1) return true;
        if (tablero[0][2] == 1 && tablero[1][1] == 1 && tablero[2][0] == 1) return true;

        return false;
    }
    public boolean ganaJugador2() {
        //Aqui comprobamos si gana el jugador2 o el robot2
        for (int i = 0; i < 3; i++) {
            if (tablero[i][0] == 2 && tablero[i][1] == 2 && tablero[i][2] == 2) return true;
            if (tablero[0][i] == 2 && tablero[1][i] == 2 && tablero[2][i] == 2) return true;
        }
        if (tablero[0][0] == 2 && tablero[1][1] == 2 && tablero[2][2] == 2) return true;
        if (tablero[0][2] == 2 && tablero[1][1] == 2 && tablero[2][0] == 2) return true;
        return false;
    }
}